# -*- coding:utf-8 -*-
'''序列化'''
from rest_framework import serializers
from .models import Banner

class BannerModelSerializer(serializers.ModelSerializer):
    '''轮播图序列化'''
    class Meta:
        model = Banner
        fields = ('image','link')