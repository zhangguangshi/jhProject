from django.contrib import admin
from goodsapp.models import *
# Register your models here.

@admin.register(GoodsModel)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ["goods_name","price","unit","stock","category"]

@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)

@admin.register(GoodsOrigin)
class GoodsOriginAdmin(admin.ModelAdmin):
    list_display = ["origin_name","origin_pic"]

@admin.register(MerchModel)
class MerchAdmin(admin.ModelAdmin):
    list_display = ["name","src","position"]


@admin.register(PackageModel)
class PackageAdmin(admin.ModelAdmin):
    list_display = ["name","src","position"]