from rest_framework.response import Response
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework import viewsets
from user.models import UserInfo
from lib.auth import JwtQueryParamsAuthentication
from lib.jwt_auth import create_token
from django.db.models import Q
from user.serializers import RegisterSerializer

class RegisterViewSet(viewsets.ModelViewSet):
    """注册视图"""
    queryset = UserInfo.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        serializer = RegisterSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



@api_view(http_method_names=['post'])
def login(self,request,*args,**kwargs):
    user = request.data.get("username")
    pwd = request.data.get("password")
    # 可以使用手机号，邮箱，姓名登录
    user_obj = UserInfo.objects.filter(Q(mobile=user,password=pwd) | Q(email=user,password=pwd) | Q(username=user, password=pwd)).first()
    if not user_obj:
        return Response({"code":1000,"error":"用户名或密码错误"})

    token = create_token({"id":user_obj.id,"name":user_obj.username})
    return Response({"code": 1001, "data": token})
