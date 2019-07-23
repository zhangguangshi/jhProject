from django.urls import path
from finapp.views import *


app_name = 'fina'

urlpatterns = [
    path('finance_con/',finance_con,name="finance_con")
]



