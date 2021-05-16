from django.db import models


class UserInfo(models.Model):
    username = models.CharField(verbose_name='用户名', max_length=32, db_index=True)  # 创建索引
    email = models.EmailField(verbose_name='邮箱', max_length=32)
    mobile_phone = models.CharField(verbose_name='手机号', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=32)
    isvip = models.BooleanField(verbose_name='会员', default=False)


class UserHistory(models.Model):
    username = models.CharField(verbose_name='用户名', max_length=32)
    mobile_phone = models.CharField(verbose_name='手机号', max_length=32)
    date = models.DateTimeField(verbose_name='日期', auto_now_add=True)
    search = models.CharField(verbose_name='搜索关键字', max_length=32)


class order(models.Model):
    mobile_phone = models.CharField(verbose_name='手机号', max_length=32)
    username = models.CharField(verbose_name='用户名', max_length=32)
    date = models.DateTimeField(verbose_name='日期', auto_now_add=True)


class PricePolicy(models.Model):
    """价格策略"""
    category_choices = {
        (1, '免费版'),
        (2, '收费版'),
        (3, '其他'),
    }
    category = models.SmallIntegerField(verbose_name='收费类型', default=2, choices=category_choices)
    title = models.CharField(verbose_name='标题', max_length=32)
    price = models.PositiveIntegerField(verbose_name='价格')  # 正整数

    project_num = models.PositiveIntegerField(verbose_name='收藏夹数')
    project_space = models.PositiveIntegerField(verbose_name='单个收藏夹空间')
    per_file_size = models.PositiveIntegerField(verbose_name='单图片大小')

    create_datetime = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)


class Project(models.Model):
    """收藏表"""
    COLOR_CHOICES = (
        (1, "#000000"),
        (2, "#ffffff"),
        (3, "#ebc656"),
        (4, "#a2d148"),
        (5, "#20BFA4"),
        (6, "#7461c2"),
        (7, "#20bfa3"),
        (8, "#56b8eb"),
        (9, "#f28033"),
        (10, "#ffc0cb"),
    )
    name = models.CharField(verbose_name='收藏文件夹名', max_length=32)
    color = models.SmallIntegerField(verbose_name='颜色', choices=COLOR_CHOICES, default=1)
    desc = models.CharField(verbose_name='收藏描述', max_length=255, null=True, blank=True)
    use_space = models.IntegerField(verbose_name='收藏夹已使用空间', default=0)
    star = models.BooleanField(verbose_name='星标', default=False)

    creator = models.ForeignKey(verbose_name='创建者', to='UserInfo', on_delete=models.DO_NOTHING)
    create_datetime = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
