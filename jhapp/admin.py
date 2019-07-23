from django.contrib import admin
from jhapp.models import *
# Register your models here.

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):

    # 后台列表页展示的字段
    list_display = ['title', 'position', 'src', 'href']
    # 后台允许搜索的字段
    search_fields = ['title']
    # 后台过滤器
    list_filter = ['position']

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):

    list_display = ["title","type","origin","time"]
    search_fields = ["title","type"]

@admin.register(NewsType)
class NewsTypeAdmin(admin.ModelAdmin):

    list_display = ["type_name","position"]
@admin.register(CompanyModel)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ["big_title","little_title","uptime"]

@admin.register(Honor)
class HoneorAdmin(admin.ModelAdmin):
    list_display = ["title","desc","time"]

@admin.register(Action_type)
class Action_typeAdmin(admin.ModelAdmin):
    list_display = ["type_name"]

@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    list_display = ["name","desc"]



# admin.site.register(Banner, BannerAdmin)
# admin.site.register(News,NewsAdmin)
# admin.site.register(NewsType,NewsTypeAdmin)