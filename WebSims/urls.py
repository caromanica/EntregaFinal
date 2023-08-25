from django.urls import path, include
from django.contrib import admin
from WebSims import views
from WebSims.views import *
from WebSims.templates import *



urlpatterns = [
    path('saludo/', saludo),
    path('inicio/', vista_inicio),
    path('registrousuarios/', registrar_usuario),
    path('registromods/', registrar_mod),
    path('listademods/', listar_mods),
    path('listadeusuarios/', listar_usuarios),
    path('usuarios', vista_usuario)
]

