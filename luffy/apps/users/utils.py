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