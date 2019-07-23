from django.contrib import admin
from teachapp.models import *
# Register your models here.

@admin.register(Teach_banner)
class TeachBannerAdmin(admin.ModelAdmin):

    # 后台列表页展示的字段
    list_display = ['title', 'position', 'src', 'href']
    # 后台允许搜索的字段
    search_fields = ['title']
    # 后台过滤器
    list_filter = ['position']


@admin.register(ExpertModel)
class ExpertAdmin(admin.ModelAdmin):
    list_display = ["name","sex","post","professional","time"]

@admin.register(VideoCategory)
class VideoTypeAdmin(admin.ModelAdmin):

    list_display = ["category"]

@admin.register(VideoType)
class VideoTypeAdmin(admin.ModelAdmin):
    list_display = ["type"]

@admin.register(VideoModel)
class VideoAdmin(admin.ModelAdmin):
    list_display = ["title","href","uptime"]



