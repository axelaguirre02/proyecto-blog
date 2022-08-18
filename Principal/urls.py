from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicioblog'),
    path('inicio/', views.inicio, name='inicio'),
    path('registro/', views.registrar_pagina, name='registro'),
    path('ingreso/', views.pagina_login, name='ingreso'),
    path('logout/', views.logout_user, name='cerrarsesion'),
]
