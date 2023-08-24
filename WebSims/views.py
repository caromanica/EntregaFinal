from django.shortcuts import render
from django.http import HttpResponse
from WebSims.models import Usuario, Modder, Mod

def saludo(request): #probando
    return HttpResponse("probando probando")
