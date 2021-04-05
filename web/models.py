from django.db import models


class UserInfo(models.Model):
    username = models.CharField(verbose_name='用户名', max_length=32, db_index=True)  # 创建索引
    email = models.EmailField(verbose_name='邮箱', max_length=32)
    mobile_phone = models.CharField(verbose_name='手机号', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=32)


class UserHistory(models.Model):
    username = models.CharField(verbose_name='用户名', max_length=32)
    mobile_phone = models.CharField(verbose_name='手机号', max_length=32)
    date = models.DateTimeField(verbose_name='日期', auto_now_add=True)
    path = models.CharField(verbose_name='路径', max_length=32)


class UserTreasure(models.Model):
    name = models.CharField(verbose_name='收藏夹名', max_length=32)
    mobile_phone = models.CharField(verbose_name='手机号', max_length=32)
    username = models.CharField(verbose_name='用户名', max_length=32)
    path = models.CharField(verbose_name='路径', max_length=32)
    date = models.DateTimeField(verbose_name='日期', auto_now_add=True)
