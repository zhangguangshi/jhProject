from django.urls import path
from userapp.views import register, login, logout, send_message, update_pwd, send_update_message,user_center,monit_detail

app_name = 'user'

urlpatterns = [
    path('register', register, name="register"),
    path('login', login, name="login"),
    path('logout', logout, name='logout'),
    path('send_message', send_message, name='send_message'),
    path('update_pwd', update_pwd, name='update_pwd'),
    path('send_update_message', send_update_message, name='send_update_message'),
    path('center/',user_center,name='center'),
    path('monit/<number>',monit_detail,name='monit')
]
