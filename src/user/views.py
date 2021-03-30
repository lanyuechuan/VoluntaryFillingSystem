from rest_framework.decorators import api_view
from .serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(http_method_names=['post'])
def register(request):
    '''注册
    '''
    serializer = RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)




def login(request):
    """用户登录"""
    passx