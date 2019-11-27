# -*- coding:utf-8 -*-

from django.urls import path,re_path
from . import views

urlpatterns = [
    path("",views.CartAPIView.as_view({"post":"add","get":"list","patch":"change_selected_statuc","delete":"delete","put":"put"})),


]