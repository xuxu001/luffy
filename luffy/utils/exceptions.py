# -*- coding:utf-8 -*-
from rest_framework.views import exception_handler
from django.db import DatabaseError
from rest_framework.response import Response
from rest_framework import status
import logging

logger = logging.getLogger("django")

def custom_exception_handler(exc,context):
    """
    自定义异常处理
    :param exc: 异常类
    :param context: 抛出异常的上下文
    :return: Response响应对象
    """
    response = exception_handler(exc,context)

    if response is None:
        if isinstance(exc,DatabaseError):
            view =context["view"]
            #数据库异常
            logger.error('[%s] %s' % (view, exc))
            response = Response('服务器储存内部错误',status=status.HTTP_507_INSUFFICIENT_STORAGE)
