from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings
import jwt
from jwt import exceptions

# 表示是验证类，这不明显query_params是get请求
class JwtQueryParamsAuthentication(BaseAuthentication):

    def authenticate(self, request):
        # 获取token并判断token得合法性
        token = request.query_params.get("token")

        # 1、切割
        # 2、解密第二段/判断是否过期
        # 3、验证第三段的合法性

        SALT = settings.SECRET_KEY
        try:
            # 看到了那个True了吗，但凡payload有返回值，就表示校验成功
            payload = jwt.decode(token, SALT, True)
        except exceptions.ExpiredSignatureError:
            raise AuthenticationFailed({"code": 1003, "error": "token已失效"})
        except jwt.DecodeError:
            raise AuthenticationFailed({"code": 1003, "error": "token认证失败"})
        except jwt.InvalidTokenError:
            raise AuthenticationFailed({"code": 1003, "error": "非法的token"})

        # 三种异常
        # 1、抛出异常，后续不再执行
        # 2、return一个元组（1，2），认证通过，在视图中，如果调用request.user就是元组的第一个值，request.auth就是元组的第二个值
        # 3、None
        return (payload, token)


