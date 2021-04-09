from rest_framework import serializers
from user.models import UserInfo
from lib.check import Check
from lib.objectid import create_objectid
import hashlib


class RegisterSerializer(serializers.ModelSerializer):
    '''注册数据模型序列化
    '''

    confirm_password = serializers.CharField()

    def validate_mobile(self, mobile):
        '''邮箱验证
        '''
        if not Check().check_mobile(mobile):
            raise serializers.ValidationError('手机号格式不正确。')
        return mobile
    
    def validate(self, data):
        '''确认密码验证
        '''
        password = data.get("password")
        confirm_password = data.get("confirm_password", "")
        if password != confirm_password:
            raise serializers.ValidationError("两次输入的密码不一致")

    def validate_password(self, password):
        '''加密密码验证
        '''
        password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        return password


    class Meta:
         model = UserInfo
         fields = '__all__'