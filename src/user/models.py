from django.db import models
from lib import create_objectid as _create_objectid
# Create your models here.



USER_ROLE = [
    (0, '普通用户'),
    (1, 'vip用户'),
    (2, 'svip用户'),
]


class User(models.Model):
    """用户表"""
    id              = models.CharField(primary_key=True, max_length=24, default=_create_objectid)
    username        = models.CharField(verbose_name='用户名', max_length=32)
    password        = models.CharField(verbose_name='密码', max_length=64)
    email           = models.EmailField(verbose_name='邮箱', max_length=32, blank=True, null=True)
    mobile          = models.CharField(verbose_name='手机号', max_length=11)
    college_score   = models.CharField(verbose_name='高考分数', max_length=6)
    area            = models.CharField(verbose_name='地区', max_length=5)
    particular_year = models.PositiveIntegerField(verbose_name='高考年份')  
    user_role       = models.IntegerField(verbose_name='用户权限', choices=USER_ROLE, default=0)   # 证明有默认值的情况下，其实是可以不用加blank=True的
    token_exp       = models.IntegerField(verbose_name='token过期时间', default=3600, blank=True)
    join_datatime   = models.DateTimeField(verbose_name='注册时间', auto_now_add=True)
    update_datetime = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    is_active       = models.IntegerField(verbose_name='激活状态', default=0, blank=True)

    class Meta:
        db_table = 'user_user'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '《{}》'.format(self.username)  