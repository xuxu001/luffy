# -*- coding:utf-8 -*-
from django.db import models
class BaseModel(models.Model):
    '''
    公共模型
    '''
    orders = models.IntegerField(verbose_name='显示顺序')
    is_show = models.BooleanField(verbose_name='是否上架', default=False)
    is_delete = models.BooleanField(verbose_name='逻辑删除', default=False)
    created_time = models.DateTimeField(verbose_name='创建时间',auto_now_add=True,null=True,blank=True)
    updated_time = models.DateTimeField(verbose_name='更新时间',auto_now=True,null=True,blank=True)

    class Meta:

        # 抽象模型，一般设置了公共模型后，数据迁移的时，不会创建数据表
        abstract=True