# -*- coding:utf-8 -*-
#celery 的任务必须卸载tasks。py的文件中，别的文件名不识别
from mycelery.main import app
from mycelery.sms.yuntongxun.sms import CCP
from .constant import SMS_EXPIRE_TIME,SMS_ID
import logging
log = logging.getLogger("django")

expire_time = SMS_EXPIRE_TIME // 60
expire_id = SMS_ID

@app.task(name = 'send_sms')
def send_sms(mobile,code):
    '''发送短信'''
    ccp = CCP()
    # print(mobile,code,expire_time,expire_id)
    result = ccp.send_template_sms(mobile, [code, expire_time], expire_id)
    log.error(result)
    # print(result)

    if result == -1:
        log.error('发送短信失败！手机号：%s'% mobile)
        log.error('短信结果%s'% result)
        return '发送失败'
    else:
        return '发送短信成功！'


@app.task(name = 'send_sms2')
def send_sms1():
    print('111')

