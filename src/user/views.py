from rest_framework.response import Response
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework import viewsets
from user.models import UserInfo
from lib.jwt_auth import create_token
from django.db.models import Q
from user.serializers import RegisterSerializer
import hashlib, json
from lib.check import Check
from lib.utils.image_code import check_code
from django_redis import get_redis_connection
from django.shortcuts import HttpResponse

# class RegisterViewSet(viewsets.ModelViewSet):
#     queryset = UserInfo.objects.all()
#     serializer_class = RegisterSerializer

#     def create(self, request, *args, **kwargs):
#         data = request.data.copy()
#         serializer = RegisterSerializer(data=data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)

@api_view(http_method_names=['post'])
def register(request, *args, **kwargs):
    data = request.data.copy()
    username  = data.get("username")
    email  = data.get("email")
    mobile  = data.get("mobile")
    college_score  = data.get("college_score")
    area  = data.get("area")
    particular_year  = data.get("particular_year")
    password  = data.get("password")

    password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    if not Check().check_mobile(mobile):
        return Response({"error":"手机号不合规则。"}, status=499)
    # 判断用户是否存在
    if UserInfo.objects.filter(username=username).first():
        return Response({"error":"该用户名已存在，请重新输入注册信息。"}, status=499)
    if UserInfo.objects.filter(email=email).first():
        return Response({"error":"该邮箱已存在，请重新输入注册信息。"}, status=499)
    if UserInfo.objects.filter(mobile=mobile).first():
        return Response({"error":"该手机号码已存在，请重新输入注册信息。"}, status=499)
    user = UserInfo.objects.create(username=username, password=password, email=email, mobile=mobile, college_score=college_score, area=area, particular_year=particular_year)
    register_user = {"username":username, "password":password,"email":email, "mobile":mobile}
    return Response({"data":register_user}, status=499)


@api_view(http_method_names=['post'])
def login(request, *args, **kwargs):
    data = request.data.copy()
    username = data.get("username")
    password  = data.get("password")
    password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    # 可以使用手机号，邮箱，姓名登录
    user_obj = UserInfo.objects.filter(Q(mobile=username,password=password) | Q(email=username,password=password) | Q(username=username, password=password)).first()
    if not user_obj:
        return Response({"error":"用户名或密码错误。"}, status=499)

    token = create_token({"id":user_obj.id,"name":user_obj.username})
    return Response({"access_token": token}, status=200)

@api_view(http_method_names=['get'])
def image_code(request):
    """生成图片验证码"""
    request.data.get("username")

    from io import BytesIO
    image_object, code = check_code()

    conn = get_redis_connection('default')

    # 写进session中
    # request.session['image_code'] = code
    # request.session.set_expiry(60)  # 60s过期

    stream = BytesIO()
    image_object.save(stream, 'png')
    # 返回图片内容
    return HttpResponse(stream.getvalue())