# -*- coding:utf-8 -*-
import xadmin
from xadmin import views

class BaseSetting(object):
    '''xadmin的基本设置'''
    enable_themes = True
    use_bootswatch = True

xadmin.site.register(views.BaseAdminView,BaseSetting)

class GlobalSettings(object):
    '''admin全局配置'''
    site_title = '学城'
    site_footer = '公司'
    menu_style = 'accordion'
xadmin.site.register(views.CommAdminView,GlobalSettings)

#轮播图
from .models import Banner
class BannerModelAdmin(object):
    list_display = ['name','orders','is_show']
xadmin.site.register(Banner,BannerModelAdmin)