from rest_framework import serializers
from user.models import UserInfo

class RegisterSerializer(serializers.ModelSerializer):
     class Meta:
        model = UserInfo
        fields = '__all__'