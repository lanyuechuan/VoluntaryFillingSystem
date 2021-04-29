from django.utils.deprecation import MiddlewareMixin
from rest_framework.response import Response
from django.conf import settings
import jwt
from jwt import exceptions

class MyMiddleware(MiddlewareMixin):
    """判断并读取jwt中用户信息中间件"""
    def process_request(self, request):
        if request.path_info in settings.WHITE_REGEX_URL_LIST:
            # 如果返回空，表示中间件通过
            return
        # 获取token并判断token得合法性
        token = request.headers.get("token")

        # 1、切割
        # 2、解密第二段/判断是否过期
        # 3、验证第三段的合法性

        SALT = settings.SECRET_KEY
        # try:
            # 传入True，代表但凡payload有返回值，就表示校验成功
        # payload = jwt.decode(token, SALT, True)
        # except exceptions.ExpiredSignatureError:
        #     return Response({"message": "token已失效"}, status=499)
        # except jwt.DecodeError:
        #     return Response({"message": "token认证失败"}, status=499)
        # except jwt.InvalidTokenError:
        #     return Response({"message": "非法的token"}, status=499)

        # jwt的token验证通过，这个payload终就是user_id和username
        # request.payload = payload
        request.token = token
        return

    
