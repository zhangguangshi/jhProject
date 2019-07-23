from django.contrib import admin
from finapp.models import *
# Register your models here.

@admin.register(Finance_form)
class TeachBannerAdmin(admin.ModelAdmin):

    # 后台列表页展示的字段
    list_display = ['name', 'sex', 'tel', 'area',"money"]
    # 后台允许搜索的字段
    search_fields = ['name',"area","money"]


