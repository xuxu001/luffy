# -*- coding:utf-8 -*-
from django.urls import path,re_path
from rest_framework_jwt.views import obtain_jwt_token
from . import views
urlpatterns =[
    #调用drf_res 登陆接口
    path("login/",obtain_jwt_token),
    #检查手机号是否注册过
    re_path("mobile/(?P<mobile>1[3-9]\d{9})/",views.CheckMobileAPIView.as_view()),
    #发送短信验证码接口
    re_path("sms/(?P<mobile>1[3-9]\d{9})/",views.SMSAPIView.as_view()),
    #注册接口
    path("reg/",views.UserAPIView.as_view()),
]