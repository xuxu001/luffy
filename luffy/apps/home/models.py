from django.db import models
from luffy.utils.models import BaseModel
# Create your models here.



class Banner(BaseModel):
    """
    轮播图
    """
    image = models.ImageField(upload_to='banner',verbose_name='轮播图',null=True,blank=True,help_text='图片大小：1920*720')
    name = models.CharField(max_length=150,verbose_name='轮播图名称')
    note = models.CharField(max_length=150,verbose_name='备注信息')
    link = models.CharField(max_length=150,verbose_name='轮播图广告地址')


    class Meta:
        db_table='banner'
        verbose_name='轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class NavInfo(BaseModel):
    '''
    导航
    '''
    NAV_POSITION=(
        (1,'top'),
        (2,'footer')
    )
    name = models.CharField(max_length=50,verbose_name='导航栏名称')
    link = models.CharField(max_length=250,verbose_name='导航栏地址')
    opt = models.SmallIntegerField(choices=NAV_POSITION,default=1,verbose_name='位置')

    class Meta:
        db_table = 'lv_nav'
        verbose_name = '导航菜单'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name
