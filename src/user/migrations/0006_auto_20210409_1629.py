# Generated by Django 2.2.1 on 2021-04-09 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20210409_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='user_role',
            field=models.IntegerField(choices=[(0, '普通用户'), (1, 'vip用户'), (2, 'svip用户')], default=0),
        ),
    ]
