# 导入django环境
import scripts.base
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
from django.conf import settings
from qcloud_cos.cos_exception import CosServiceError


def create_bucket(bucket, region="ap-chengdu"):
    """创建桶和区域"""

    config = CosConfig(Region=region, SecretId=settings.COS_SECRET_ID, SecretKey=settings.COS_SECRET_KEY)
    client = CosS3Client(config)
    client.create_bucket(
        Bucket=bucket,
        ACL="public-read"  # private  /  public-read / public-read-write
    )

if __name__ == "__main__":
    create_bucket("dasd-dsfdsf-1300792884")

def upload_file(bucket, region, file_object, key):
    config = CosConfig(Region=region, SecretId=settings.COS_SECRET_ID, SecretKey=settings.COS_SECRET_KEY)
    client = CosS3Client(config)

    # 这个方式时可以上传文件对象！！！！！！对象
    # 因为我们基本上都是前端传id过来，我们能拿到文件对象
    response = client.upload_file_from_buffer(
        Bucket=bucket,
        Body=file_object,  # 文件对象
        Key=key  # 上传到桶之后的文件名
    )

    # https://wangyang-1251317460.cos.ap-chengdu.myqcloud.com/p1.png
    image_url = "https://{}.cos.{}.myqcloud.com/{}".format(bucket, region, key)
    return image_url


def delete_file(bucket, region, key):
    """传入桶，区域，文件名"""
    config = CosConfig(Region=region, SecretId=settings.TENCENT_COS_ID, SecretKey=settings.TENCENT_COS_KEY)
    client = CosS3Client(config)

    client.delete_object(
        Bucket=bucket,
        Key=key
    )


def check_file(bucket, region, key):
    """校验etag值是否跟前端对的上，对的上才用，但是我们file的form组件中没有使用，没必要"""
    config = CosConfig(Region=region, SecretId=settings.TENCENT_COS_ID, SecretKey=settings.TENCENT_COS_KEY)
    client = CosS3Client(config)

    data = client.head_object(
        Bucket=bucket,
        Key=key
    )

    return data


def delete_file_list(bucket, region, key_list):
    """批量删文件跟删除文件的区别就是传个列表进来，但是得构造成字典，放进Object对象"""
    config = CosConfig(Region=region, SecretId=settings.TENCENT_COS_ID, SecretKey=settings.TENCENT_COS_KEY)
    client = CosS3Client(config)
    objects = {
        "Quiet": "true",
        "Object": key_list
    }
    client.delete_objects(
        Bucket=bucket,
        Delete=objects
    )


def credential(bucket, region):
    """ 获取cos上传临时凭证 """
    from sts.sts import Sts

    config = {
        # 临时密钥有效时长，单位是秒（30分钟=1800秒）
        'duration_seconds': 5,
        # 固定密钥 id
        'secret_id': settings.COS_SECRET_ID,
        # 固定密钥 key
        'secret_key': settings.COS_SECRET_KEY,
        # 换成你的 bucket
        'bucket': bucket,
        # 换成 bucket 所在地区
        'region': region,
        # 这里改成允许的路径前缀，可以根据自己网站的用户登录态判断允许上传的具体路径
        # 例子： a.jpg 或者 a/* 或者 * (使用通配符*存在重大安全风险, 请谨慎评估使用)
        'allow_prefix': '*',
        # 密钥的权限列表。简单上传和分片需要以下的权限，其他权限列表请看 https://cloud.tencent.com/document/product/436/31923
        'allow_actions': [
            # "name/cos:PutObject",
            # 'name/cos:PostObject',
            # 'name/cos:DeleteObject',
            # "name/cos:UploadPart",
            # "name/cos:UploadPartCopy",
            # "name/cos:CompleteMultipartUpload",
            # "name/cos:AbortMultipartUpload",
            "*",
        ],

    }

    sts = Sts(config)
    result_dict = sts.get_credential()
    return result_dict


def delete_bucket(bucket, region):
    """ 删除桶 """
    # 删除桶中所有文件，腾讯对象存储只有删空桶的api
    # 删除桶中所有碎片
    # 删除桶
    config = CosConfig(Region=region, SecretId=settings.COS_SECRET_ID, SecretKey=settings.COS_SECRET_KEY)
    client = CosS3Client(config)  # 想拿操作对象

    # 如果压根没有这个桶会报CosServiceError异常
    try:
        # 找到文件 & 删除，list_objects(桶)可以返回桶中带的所有文件， 点进去看源码MaxKeys=1000
        # 会返回一个文件字典对象，一次最多返回一千个，如果桶中文件有一千个及以上，要获取多次
        while True:
            part_objects = client.list_objects(bucket)
            # print('返回值是个字典，有这些结构：\n' + part_objects)
            # break

            # 如果字典中Contents字段为空，说明桶里没文件
            contents = part_objects.get('Contents')
            # 为空说明删完，跳出
            if not contents:
                break

            # 批量删除delete_objects方法，得构造一个特殊的结构
            objects = {
                "Quiet": "true",
                "Object": [{'Key': item["Key"]} for item in contents]
            }
            client.delete_objects(bucket, objects)

            # 返回的对象中是否有截断的。
            if part_objects['IsTruncated'] == "false":
                break

        # 找到碎片 & 删除
        while True:
            # 也是返回最大一千个
            part_uploads = client.list_multipart_uploads(bucket)
            uploads = part_uploads.get('Upload')
            if not uploads:
                break
            for item in uploads:
                client.abort_multipart_upload(bucket, item['Key'], item['UploadId'])
            if part_uploads['IsTruncated'] == "false":
                break

        # 文件，碎片都删完了，变成空桶
        client.delete_bucket(bucket)

    except CosServiceError as e:
        pass
