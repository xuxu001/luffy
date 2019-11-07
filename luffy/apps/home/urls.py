# -*- coding:utf-8 -*-
from django.urls import path,re_path
from . import views
urlpatterns =[
    path("banner/",views.BannerListAPIView.as_view()),
    path("nav/",views.NavListAPIView.as_view())
]