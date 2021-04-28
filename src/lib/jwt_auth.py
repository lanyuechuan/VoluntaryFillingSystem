import jwt
import datetime
from django.conf import settings

def create_token(payload, timeout=settings.JWT_TIMEOUT):

    SALT = settings.SECRET_KEY

    # 构造header
    headers = {
        'typ': 'jwt',
        'alg': 'HS256'
    }
    # 构造payload
    payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(minutes=timeout)  # 超时时间自定义
    token = jwt.JWT().encode(payload=payload, key=SALT, alg="HS256", optional_headers=headers).decode('utf-8')
    return token
