from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from adm_interface import views

app_name = 'adm_interface'

urlpatterns = [
    path('', views.loginPage, name='login'),
    path('main', views.main, name='main'),
    path('domain', views.domain, name='domain'),
    path('deletedom/<int:id>', views.deletedom, name='deletedom'),
    path('document', views.document, name='document'),
    path('url', views.url, name='url'),
    path('<int:id>', views.updateurl, name='updateurl'),
    #path('updateurl/<int:id>/', views.updateurl, name='updateurl'),
    path('deleteurl/<int:id>', views.deleteurl, name='urldom'),
    path('test', views.test, name='test'), # remove this path later (for testing purpose only)
    path('config/<int:id>', views.config, name='config'),
<<<<<<< HEAD
=======
    # path('check_config', views.check_config, name='check_config'),
    # path('img_config', views.img_config, name='img_config'),
    # path('text_config', views.text_config, name='text_config'),
    # path('headline_config', views.headline_config, name='headline_config'),
    # path('time_config', views.time_config, name='time_config'),
#path('api/', include('api.urls')),

>>>>>>> 9486038fbc377cc4d0f56ccbf5cacbada19afb42
]
urlpatterns += staticfiles_urlpatterns()

