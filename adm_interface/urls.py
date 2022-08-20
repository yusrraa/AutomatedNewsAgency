from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from adm_interface import views

app_name = 'adm_interface'

urlpatterns = [
    path('', views.loginPage, name='login'),
    path('logout',views.logout,name='logout'),
    path('main', views.main, name='main'),
    path('domain', views.domain, name='domain'),
    path('deletedom/<int:id>', views.deletedom, name='deletedom'),
    path('document', views.document, name='document'),
    path('url', views.url, name='url'),
    path('<int:id>', views.updateurl, name='updateurl'),
    path('deleteurl/<int:id>', views.deleteurl, name='urldom'),
    path('disableurl/<int:id>', views.disableurl, name ='disableurl' ),
    path('test', views.test, name='test'), # remove this path later (for testing purpose only)
    path('config/<int:id>', views.config, name='config'),
#path('api/', include('api.urls')),

]
urlpatterns += staticfiles_urlpatterns()

