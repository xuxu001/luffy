from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    '''unique=true 在同一个表中只能出现一次，唯一索引'''
    mobile = models.CharField(verbose_name='手机号',max_length=15,unique=True)
    avatar = models.ImageField(upload_to='avatar',verbose_name='头像',null=True,blank=True,help_text='图片大小：256*256')

    class Meta:
        db_table = 'ly_users'
        verbose_name = '用户'
        verbose_name_plural = verbose_name