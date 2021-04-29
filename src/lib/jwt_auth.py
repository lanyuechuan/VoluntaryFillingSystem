import jwt
import datetime
from django.conf import settings

def create_token(payload, timeout=settings.JWT_TIMEOUT):

    SALT = settings.SECRET_KEY
    # 构造header，我的token是通过jwt的方式，用的HS256加密
    headers = {
        'typ': 'jwt',
        'alg': 'HS256'
    }
    # 构造payload
    payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(minutes=timeout)  # 超时时间自定义
    token = jwt.encode(payload=payload, key=SALT, algorithm="HS256", headers=headers).decode('utf-8')
    return token
