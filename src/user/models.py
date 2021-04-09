from django.db import models
from lib import create_objectid as _create_objectid
# Create your models here.



USER_ROLE = [
    (0, '普通用户'),
    (1, 'vip用户'),
    (2, 'svip用户'),
]


class UserInfo(models.Model):
    """用户表"""
    id              = models.CharField(primary_key=True, max_length=24, default=_create_objectid)
    username        = models.CharField(verbose_name='姓名', max_length=32)
    password        = models.CharField(verbose_name='密码', max_length=128)
    email           = models.EmailField(verbose_name='邮箱', max_length=32, blank=True, null=True)
    mobile          = models.CharField(verbose_name='手机号', max_length=11)
    college_score   = models.CharField(verbose_name='高考分数', max_length=6)
    area            = models.CharField(verbose_name='地区', max_length=5)
    particular_year = models.PositiveIntegerField(verbose_name='高考年份')
    user_role       = models.IntegerField(choices=USER_ROLE, default=0)