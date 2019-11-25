# -*- coding:utf-8 -*-
#主程序

import os
from celery import Celery


#创建celery实例对象
app = Celery("luffy")

#吧celery和django进行组合，识别和加载django的配置文件

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'luffy.settings.dev')
import django
django.setup()
#通过app对象加载配置
app.config_from_object("mycelery.config")




#加载任务
#参数必须是一个列表，里面的每一个任务都是任务的路径名称
# app.register_task(["任务1","任务2"])
app.autodiscover_tasks(["mycelery.sms"])




#启动celery的命令z
# 下载eventlet

# celery -A mycelery.main worker --loglevel=info -P eventlet


#启动redis
# redis-server redis.windows.conf



