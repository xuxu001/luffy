# -*- coding:utf-8 -*-
from rest_framework import serializers
from .models import Order,OrderDetail
from datetime import datetime
import random
from course.models import Course,CourseExpire
from django_redis import get_redis_connection
class OrderModerSerializer(serializers.ModelSerializer):
    '''订单序列化器'''
    # coupon = CouponSerializer()
    #
    class Meta:
        model = Order
        fields =['id','order_title','total_price','real_price','order_number',
                 'order_status','pay_type','use_credit','credit','use_coupon','coupon',
                 'pay_time',]
        extra_kwargs ={
            "id":{"read_only":True},
            "order_title":{"read_only":True},
            "total_price":{"read_only":True},
            "real_price":{"read_only":True,},
            "order_number":{"read_only":True},
            "order_status":{"read_only":True},
            "pay_time":{"read_only":True},
            # "user":{"read_only":True},
            "pay_type":{"required":True},
            "use_credit":{"required":True},
            "credit":{"required":True,"min_value":0},
            "use_coupon":{"required":True},
        }

    # def create(self, validated_data):
    #     '''
    #     生成订单
    #     :param validated_data:
    #     :return:
    #     '''
    #
    #     #接受客户端提交的数据
    #     pay_type = validated_data.get("pay_type")
    #     use_credit = validated_data.get("use_credit")
    #     credit = validated_data.get("credit")
    #     use_coupon = validated_data.get("use_coupon")
    #     coupon = validated_data.get("coupon",None)
    #
    #
    #     #生成必要参数
    #     user_id = 1 #todo 学习怎么从序列化器中获取试图中的数据
    #     order_title = '课程购买'
    #     order_number = datetime.now().strftime("%Y%m%d%H%M%S") + ("%06d"%user_id)+("%06d"%random.randint(0,999999))
    #     order_status = 0
    #     #从购物车中获取订单信息
    #
    #     #生成订单记录
    #     order = super().create({
    #         "order_title":order_title,
    #         "total_price":0,
    #         "real_price":0,
    #         "order_number": order_number,
    #         "order_status": order_status,
    #         "pay_type":pay_type,
    #         "use_credit":use_credit,
    #         "credit":credit if use_credit else None,
    #         "use_coupon":use_coupon,
    #         "coupon":coupon,
    #         "order_desc":"",
    #         "user_id":user_id,
    #     })
    #     #链接redis
    #     redis = get_redis_connection("cart")
    #     #
    #     # #从购物车获取订单信息
    #     course_set = redis.smembers("selected_%s"% user_id)
    #     cart_list = redis.hgetall("cart_%s"% user_id)
    #     for course_id_bytes in course_set:
    #
    #         #有效期选项
    #         course_expire_bytes = cart_list[course_id_bytes]
    #         expire_id = int( course_expire_bytes.decode() )
    #         print(expire_id)
    #         course_id = int( course_id_bytes.decode() )
    #         print(course_id)
    #         course = Course.orders.filter(pk=course_id)
    #
    #         # try:
    #         #     course = Course.orders.get(pk=course_id)
    #         # except:
    #         #     return serializers.ValidationError("课程不存在")
    #     # #     #提取课程的有效期选项
    #         if expire_id > 0:
    #             course_expire = CourseExpire.objects.get(pk=expire_id)
    #             price = course_expire.price
    #         else:
    #             price = course.price
    #
    #         #获取
    #
    #         # 生成订单详情
    #         OrderDetail.objects.create(
    #             Order = order,
    #             course = course,
    #             expire = expire_id,
    #             price =price,
    #             real_price = course.get_real_price(price),
    #             discount_name = course.discount_type,
    #         )
    #
    #
    #
    #     #生成订单详情记录
    #
    #     #记录订单的总价和实价
    #
    #     #返回订单模型
    #
    #     return order