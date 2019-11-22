# -*- coding:utf-8 -*-
from django.urls import path,re_path
from . import views
urlpatterns =[
    #首页轮播图接口
    path("banner/",views.BannerListAPIView.as_view()),
    #导航栏接口
    path("nav/",views.NavListAPIView.as_view())
]