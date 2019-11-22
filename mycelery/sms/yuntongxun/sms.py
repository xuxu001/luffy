# -*- coding:utf-8 -*-
# coding=gbk

# coding=utf-8

# -*- coding: UTF-8 -*-

from .CCPRestSDK import REST
from mycelery.sms.constant import SMS_ACCOUNTSID,SMS_ACCOUNTTOKEN,SMS_APPID,SMS_SERVERIP

# 主帐号
accountSid = SMS_ACCOUNTSID;

# 主帐号Token
accountToken = SMS_ACCOUNTTOKEN;

# 应用Id
appId = SMS_APPID;

# 请求地址，格式如下，不需要写http://
serverIP = SMS_SERVERIP;

# 请求端口
serverPort = '8883';

# REST版本号
softVersion = '2013-12-26';


# 发送模板短信
# @param to 手机号码
# @param datas 内容数据 格式为数组 例如：{'12','34'}，如不需替换请填 ''
# @param $tempId 模板Id
#
# def sendTemplateSMS(to, datas, tempId):
#     # 初始化REST SDK
#     rest = REST(serverIP, serverPort, softVersion)
#     rest.setAccount(accountSid, accountToken)
#     rest.setAppId(appId)
#
#     result = rest.sendTemplateSMS(to, datas, tempId)
#     for k, v in result.iteritems():
#
#         if k == 'templateSMS':
#             for k, s in v.iteritems():
#                 print
#                 '%s:%s' % (k, s)
#         else:
#             print
#             '%s:%s' % (k, v)

class CCP(object):
    instance = None

    def __new__(cls):
        # 判断CCP类有没有已经创建好的对象
        if cls.instance is None:
            obj = super(CCP, cls).__new__(cls)

            # 初始化REST SDK
            obj.rest = REST(serverIP, serverPort, softVersion)
            obj.rest.setAccount(accountSid, accountToken)
            obj.rest.setAppId(appId)

            cls.instance = obj

        return cls.instance

    def send_template_sms(self,to,datas,temp_id):
        result = self.rest.sendTemplateSMS(to,datas,temp_id)
        print(result)
        if result.get("statusCode") == "000000":
            return 0
        else:
            return -1

if __name__ == "__main__":
    ccp = CCP()



