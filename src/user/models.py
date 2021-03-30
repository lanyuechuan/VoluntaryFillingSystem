from django.db import models
from lib import create_objectid as _create_objectid
# Create your models here.


class UserInfo(models.Model):
    """用户表"""
    id       = models.CharField(primary_key=True, max_length=24, default=_create_objectid)
    username = models.CharField(verbose_name='用户名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=32)
    email    = models.EmailField(verbose_name='邮箱', max_length=32, blank=True, null=True)
    mobile   = models.CharField(verbose_name='手机号', max_length=11)
    
