from django.shortcuts import render
from rest_framework.views import APIView
from .models import User
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from luffy.libs.yuntongxun.sms import CCP
from luffy.settings.constant import SMS_EXPIRE_TIME,SMS_ID,SMS_INTERVAL_TIME
import random
from django_redis import get_redis_connection
import logging
log = logging.getLogger("django")
class CheckMobileAPIView(APIView):
    def get(self,request,mobile):
        result = False
        try:
            User.objects.get(mobile=mobile)
            result = False
            code = status.HTTP_400_BAD_REQUEST
        except User.DoesNotExist:
            result = True
            code = status.HTTP_200_OK
        return Response({'result':result},status=code)



class SMSAPIView(APIView):
    def get(self,request,mobile):
        #接受手机号码，验证是否已注册
        log.error(mobile)
        try:
            User.objects.get(mobile=mobile)
            return Response('当前手机号码已被注册', status=status.HTTP_400_BAD_REQUEST)
        except:
            pass



        #生成短信号码并把短信和手机号保存到redis中
        code = "%06d"%random.randint(0,99999)
        expire_time = SMS_EXPIRE_TIME // 60
        expire_id = SMS_ID

        try:
            # 引入redis

            redis = get_redis_connection("sms_code")
            mobile_interver = redis.get("mobile_%s"%mobile)
            if mobile_interver:
                return Response({'msg':'请稍后再试'},status = status.HTTP_400_BAD_REQUEST)
            #在以后开发中如果要一次性写入多条redis命令，建议使用事务操作
            pip = redis.pipeline()
            pip.multi()
            # 设置间隔时间
            pip.setex("mobile_%s"%mobile,SMS_INTERVAL_TIME,"_") #"-"表示占位符，没有任何意义


            pip.setex('sms_%s'%mobile,expire_time,code)

            #执行管道中所有命令
            pip.execute()
            #发送短信
            # 参数说明，接受短信的手机号，【短信验证码，短信有效期】，短信模板id
            # 模板id在测试阶段是1
            ccp = CCP()
            result = ccp.send_template_sms(mobile, [code, expire_time], expire_id)
            if result == -1:
                log.error('发送短信失败！手机号：%s'%mobile)
                return Response({'msg':'短信发送失败'},status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            log.error('发送短信失败！')
            return Response({'msg':'服务器异常'},status = status.HTTP_507_INSUFFICIENT_STORAGE)

        return Response({'msg':'短信发送成功'},status = status.HTTP_200_OK)







