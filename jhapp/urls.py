# -*- coding:utf-8 -*-
"""
梅花香自苦寒来！
Author:zhang G.S
Time:  2019/1/17 21:49
File Name: urls
"""
from django.urls import path
from jhapp.views import *

app_name = 'jh'

urlpatterns = [
    # 首页的url
    path('index/',index,name='index'),
    # 农业金融的url
    path('finance/',finance,name='finance'),
    # 新闻页面的url 带参数分类 以及分页
    path('news/<type_id>/<page_num>',news,name='news'),
    # 关于公司页面的url
    path('company',company,name="company"),
]









