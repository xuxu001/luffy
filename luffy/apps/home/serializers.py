# -*- coding:utf-8 -*-
'''序列化'''
from rest_framework import serializers
from .models import Banner,NavInfo

class BannerModelSerializer(serializers.ModelSerializer):
    '''轮播图序列化'''
    class Meta:
        model = Banner
        fields = ['image','link']


class NavModelSerializer(serializers.ModelSerializer):
    '''导航菜单序列化'''
    class Meta:
        model = NavInfo
        fields = ['name','link','opt']
