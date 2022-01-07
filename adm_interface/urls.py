from django.contrib import admin
from django.urls import path, include
from adm_interface import views

app_name = 'adm_interface'

urlpatterns = [
    path('', views.login, name='login'),
    path('main', views.main, name='main'),
    path('domain', views.domain, name='domain'),
    path('document', views.document, name='document'),
    path('url', views.url, name='url'),
    path('test', views.test, name='test'), # remmove this path later (for testing purpose only)
]

