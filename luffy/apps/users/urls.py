# -*- coding:utf-8 -*-
from django.urls import path,re_path
from rest_framework_jwt.views import obtain_jwt_token
from . import views
urlpatterns =[
    #调用drf_res 登陆接口
    path("login/",obtain_jwt_token),
    re_path("mobile/(?P<mobile>1[3-9]\d{9})/",views.CheckMobileAPIView.as_view()),
    re_path("sms/(?P<mobile>1[3-9]\d{9})/",views.SMSAPIView.as_view()),
]