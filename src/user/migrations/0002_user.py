# Generated by Django 2.2.1 on 2021-05-11 06:26

from django.db import migrations, models
import lib.objectid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(default=lib.objectid.create_objectid, max_length=24, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=32, verbose_name='用户名')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
                ('email', models.EmailField(blank=True, max_length=32, null=True, verbose_name='邮箱')),
                ('mobile', models.CharField(max_length=11, verbose_name='手机号')),
                ('college_score', models.CharField(max_length=6, verbose_name='高考分数')),
                ('area', models.CharField(max_length=5, verbose_name='地区')),
                ('particular_year', models.PositiveIntegerField(verbose_name='高考年份')),
                ('user_role', models.IntegerField(choices=[(0, '普通用户'), (1, 'vip用户'), (2, 'svip用户')], default=0, verbose_name='用户权限')),
                ('token_exp', models.IntegerField(blank=True, default=3600, verbose_name='token过期时间')),
                ('join_datatime', models.DateTimeField(auto_now_add=True, verbose_name='注册时间')),
                ('update_datetime', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('is_active', models.IntegerField(blank=True, default=0, verbose_name='激活状态')),
            ],
            options={
                'verbose_name': '用户表',
                'verbose_name_plural': '用户表',
                'db_table': 'user_user',
            },
        ),
    ]
