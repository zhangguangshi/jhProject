from django.contrib import admin
from userapp.models import UserModel,MonitModel
# Register your models here.


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('username', 'phone')
    search_fields = ('phone',)


@admin.register(MonitModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'number')




