"""autonewsagn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


admin.site.site_header = 'Automated News Channel'
admin.site.site_title = 'automated news channel'
admin.site.index_title = 'Welcome to Automated News Channel'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.main, name='main'),
    path('sports',views.sports, name='sports'),
    path('tech',views.tech, name='tech'),
    path('entertm',views.entertm, name='entertm'),
    path('reporter_video',views.reporter_video, name='reporter_video'),
    path('adm/', include('adm_interface.urls'))

]

urlpatterns += staticfiles_urlpatterns()