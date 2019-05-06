from django.db import models
# Create your models here.


class User(models.Model):
    '''用户表'''
    gender = (
        ('male','男'),
        ('female','女'),
    )

    '''unique=True,重复出现的记录仅保留一条,若指定为False，则筛选出所有符合条件的记录。默认值为 False。'''
    name = models.CharField(max_length=200,unique=True)  # 名字
    password = models.CharField(max_length=256)  # 密码
    email = models.EmailField(unique=True)  # 邮箱
    # 性别设置根据gender字段展示，默认展示男
    sex = models.CharField(max_length=32, choices=gender, default='男')  #性别
    # 创建时间，默认为当前的时间
    c_time = models.DateTimeField(auto_now_add=True)

    '''前端返回展示用户的姓名'''
    def __str__(self):
        return  self.name


    class Meta:
        ordering = ['c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'