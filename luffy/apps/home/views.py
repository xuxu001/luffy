from django.shortcuts import render
from rest_framework.generics import ListAPIView
# Create your views here.
from .models import Banner,NavInfo
from luffy.settings import constant
from .serializers import BannerModelSerializer,NavModelSerializer

class BannerListAPIView(ListAPIView):
    queryset = Banner.objects.filter(is_delete=False,is_show=True).order_by('-orders')[:constant.BANNER_LENGTH]
    serializer_class = BannerModelSerializer

class NavListAPIView(ListAPIView):
    queryset = NavInfo.objects.filter(is_delete=False,is_show=True).order_by('-orders')[:constant.NAV_LENGTH]
    serializer_class = NavModelSerializer