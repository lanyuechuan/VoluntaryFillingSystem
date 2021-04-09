import hashlib
import uuid

from django.conf import settings

def md5(string):
    """MD5加密"""
################################### 用于密码加密后入库，再form中完成的
    hash_object= hashlib.md5(settings.SECRET_KEY.encode("utf8"))
    hash_object.update(string.encode("utf8"))
    return hash_object.hexdigest()



def uid(string):
    data = "{}-{}".format(str(uuid.uuid4()), string)
    # 再整体做个md5，
    return md5(data)