"""jhweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jh/',include('jhapp.urls',namespace='jh')),
    path('jh/goods/',include('goodsapp.urls',namespace='goods')),
    path('jh/teach/',include('teachapp.urls',namespace='teach')),
    path('jh/cir/',include('cirapp.urls',namespace='cir')),
    path('jh/user/',include('userapp.urls',namespace='user')),
    path('jh/fin/',include('finapp.urls',namespace='fina'))
]


from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
