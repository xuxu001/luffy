# -*- coding:utf-8 -*-

import xadmin
from xadmin import views


from .models import Order,OrderDetail

class OrderModelAdmin(object):
    '''订单管理模型类'''
    pass
xadmin.site.register(Order,OrderModelAdmin)



class OrderDetailModelAdmin(object):
    '''订单详情管理模型类'''
    pass
xadmin.site.register(OrderDetail,OrderDetailModelAdmin)

