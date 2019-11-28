# -*- coding:utf-8 -*-
from rest_framework.pagination import PageNumberPagination

class CoursePageNumberPagination(PageNumberPagination):
    '''课程列表的分页器'''
    page_query_param = 'page'   #页码参数
    page_size_query_param = 'page_size' #单页数据量
    page_size = 10                   #每页显示几个数据
    max_page_size = 20               # 允许客户端设置的单页数据量