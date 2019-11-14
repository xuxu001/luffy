# -*- coding:utf-8 -*-

from rest_framework import serializers
from .models import User
from rest_framework_jwt.settings import api_settings
import re
from django_redis import get_redis_connection

import logging
log = logging.getLogger("django")
class UserModelSerializer(serializers.ModelSerializer):
    sms_code = serializers.CharField(write_only=True,max_length=6,min_length=6,label='手机短信',help_text='手机信息')
    token = serializers.CharField(read_only=True,label='jwt的token')
    class Meta:
        model = User
        fields = ['mobile','password','sms_code','token','id','username']
        extra_kwargs = {
            "id": {
                "read_only": True
            },

            "username":{
                "read_only":True
            },
            "password":{
                "write_only":True
            },
            "mobile": {
                "write_only": True
            }
        }

    def validate(self,data):
       #接受数据
        mobile = data.get("mobile")
        sms_code = data.get("sms_code")
        password = data.get("password")

        #验证手机号
        if not re.match("^1[3-9]\d{9}$",mobile):
           raise serializers.ValidationError("手机号格式错误!")

        #验证手机短信
        try:
            redis = get_redis_connection("sms_code")
        except:
            log.error('redis链接错误')
            raise serializers.ValidationError("服务器出错了")
        #获取redis中验证码
        try:
            real_sms_code = redis.get("sms_%s" % mobile).decode()
            print(real_sms_code)
        except:
            raise serializers.ValidationError("手机短信不存在或者已过期")
        #验证是否正确
        if sms_code != real_sms_code:
            raise serializers.ValidationError('短信验证失败')

        #验证手机是否注册了
        try:
           User.objects.get(mobile=mobile)
           raise serializers.ValidationError('手机号已经注册了')
        except:
           pass

        #验证密码长度

        if len(password) <6 or len(password)>16:
           raise serializers.ValidationError('密码长度错误')

        return data

    def create(self,validated_data):
        mobile = validated_data.get("mobile")
        password = validated_data.get("password")
        try:
            user = User.objects.create_user(
                mobile=mobile,
                username=mobile,
                password=password,
            )
        except:
            log.error('创建用户失败mobile=%s'%mobile)
            raise serializers.ValidationError("创建注册用户失败")

        #注册成功后，默认当前用户为登陆状态，返回登陆的token
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        user.token = jwt_encode_handler(payload)
        return user




