# -*- coding:utf-8 -*-
#针对drf_jwt返回多个值

def jwt_response_payload_handler(token,user=None,request=None):
    '''

    :param token: 在登陆信息通过验证以后，生成jwt字符串
    :param user: 在登陆信息通过验证后，从数据库查询出来的登陆用户信息模型对象
    :param request: 在本次客户端提交数据时，发送过来的请求
    :return:
    '''

    return {
        'token':token,
        'user_id':user.id,
        'user_name':user.username
    }


#实现多条件登陆
from django.contrib.auth.backends import ModelBackend
from .models import User
import re

def get_account_by_username(account):
    '''

    :param account:账号，可以是用户名，或者手机号
    :return: User对象 或者None
    '''
    try:
        if re.match('^1[3-9]\d{9}$', account):
            # 账号为手机号
            user = User.objects.get(mobile=account)
        # elif re.match("@"):
        #     user = User.objects.get(email=account)
        else:
            # 账号为用户名
            user = User.objects.get(username=account)
    except User.DoesNotExist:
        return None
    else:
        return user

class UsernameMobileAuthBackend(ModelBackend):
    '''
    自定义用户名或者手机号认证
    '''
    def authenticate(self,request,username=None,password=None,**kwargs):
        user = get_account_by_username(username)
        # if user is not None and user.check_password(password):
        #     return user
        # else:
        #     return None
        if user is None:
            return None
        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        # if user.check_password(password):
        #     return user


