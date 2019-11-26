# -*- coding:utf-8 -*-
from django.urls import path,re_path
from . import views

urlpatterns = [
    path("category/",views.CourseCategoryAPIView.as_view()),
    path("",views.CourseAPIView.as_view()),
    re_path("(?P<pk>\d+)/",views.CourseRetrieveAPIView.as_view()),
]