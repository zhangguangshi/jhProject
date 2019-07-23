# -*- coding:utf-8 -*-
"""
梅花香自苦寒来！
Author:zhang G.S
Time:  2019/2/27 19:38
File Name: urls
"""
from django.urls import path
from goodsapp.views import *

app_name = 'goods'

urlpatterns = [
   path('',goods,name="goods"),
   path('list/<int:category_id>',goods_list,name="goods_list"),
   path('detail/<int:goods_id>/<sort>',goods_detail,name="goods_detail"),
]

