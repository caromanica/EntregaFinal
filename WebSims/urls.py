from django.urls import path, include
from django.contrib import admin
from WebSims import views
from WebSims.views import *



urlpatterns = [
    path('saludo/', saludo),
    path('registrousuarios/', registrar_usuario),
    path('registromods/', registrar_mod),
    path('listademods/', listar_mods),
    path('listadeusuarios/', listar_usuarios)
     
]

