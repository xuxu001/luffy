# -*- coding:utf-8 -*-
from rest_framework import serializers
from .models import CourseCategory,Course,Teacher
class CourseCategorySerializer(serializers.ModelSerializer):
    '''课程分类信息'''
    class Meta:
        model = CourseCategory
        fields =["id","name"]




# 增加模型字段获取数据
# class CourseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Course
#         fields =["id","name","course_img","students","lessons","pub_lessons","price","teacher","teacher_name"]

#序列化嵌套
#序列化器嵌套【被乔涛的序列化器必须声明对应的字段为模型原有的外键字段，同时这个被嵌套的序列化必须声明才能进行调用】
#如果嵌套的序列化器数据有多条，则需要在调用序列化器时声明many=True
class TeacherSeruakuzer(serializers.ModelSerializer):
    '''课程列表的老师信息'''
    class Meta:
        model = Teacher
        fields = ["id","name","role","title","signature","brief","image"]

class CourseSerializer(serializers.ModelSerializer):
    '''课程列表的基本信息'''
    teacher = TeacherSeruakuzer()
    class Meta:
        model = Course
        fields =["id","name","course_img","students","lessons","pub_lessons","price_real","teacher","lessom_list"]

class CourseRetrieveSerializer(serializers.ModelSerializer):
    teacher = TeacherSeruakuzer()
    class Meta:
        model = Course
        fields = ['id','name','course_img','students','lessons','pub_lessons','price','teacher','brief','level_name']