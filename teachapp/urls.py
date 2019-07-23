# -*- coding:utf-8 -*-
"""
梅花香自苦寒来！
Author:zhang G.S
Time:  2019/2/28 16:43
File Name: urls
"""

from django.urls import path
from teachapp.views import *

app_name = 'teach'

urlpatterns = [
    path('',teach,name="teach"),
    path('list/<type_name>',video_list,name="video_list"),
    path('detail/<video_id>',video_detail,name="video_detail"),
    path('expert/<expert_id>',experts,name="expert_detail")
]

