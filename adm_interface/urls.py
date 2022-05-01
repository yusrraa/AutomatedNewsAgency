from django.contrib import admin
from django.urls import path, include
from adm_interface import views

app_name = 'adm_interface'

urlpatterns = [
    path('', views.login, name='login'),
    path('main', views.main, name='main'),
    path('domain', views.domain, name='domain'),
    path('deletedom/<int:id>', views.deletedom, name='deletedom'),
    path('document', views.document, name='document'),
    path('url', views.url, name='url'),
    path('deleteurl/<int:id>', views.deleteurl, name='urldom'),
    path('test/<int:id>', views.test, name='test'), # remmove this path later (for testing purpose only)
    path('config/<int:id>', views.config, name='config'),
    path('check_config', views.check_config, name='check_config'),
    path('img_config', views.img_config, name='img_config'),
    path('text_config', views.text_config, name='text_config'),
    path('headline_config', views.headline_config, name='headline_config'),
    path('time_config', views.time_config, name='time_config'),

]

