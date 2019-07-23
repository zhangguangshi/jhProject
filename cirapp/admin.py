from django.contrib import admin
from cirapp.models import *
# Register your models here.

@admin.register(PurchaserModel)
class PurchaserAdmin(admin.ModelAdmin):
    list_display = ["name","pic","desc"]

@admin.register(PurchProductsModel)
class PurProAdmin(admin.ModelAdmin):
    list_display = ['title',"purchaser","desc"]
