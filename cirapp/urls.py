# -*- coding:utf-8 -*-

from django.urls import path
from cirapp.views import *

app_name = 'cir'

urlpatterns = [
    path('',cir,name='cir'),
    path('detail/<int:pur_id>',cir_detail,name="cir_detail"),
]




