from django.contrib import admin
from django.urls import path, include
from adm_interface import views

urlpatterns = [
    path('', views.login, name='login'),
    path('main', views.main, name='main'),
    path('supadmin', views.supadmhome, name='supadm'),
]