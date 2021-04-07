from rest_framework import serializers
from user.models import UserInfo
from lib.check import Check


class RegisterSerializer(serializers.ModelSerializer):
    '''注册数据模型序列化
    '''

    confim_password = serializers.CharField()

    def validate_mobile(self, mobile):
        '''邮箱验证
        '''
        if not Check().check_mobile(mobile):
            raise serializers.ValidationError('手机号格式不正确。')
        return mobile


    class Meta:
         model = UserInfo
         fields = '__all__'