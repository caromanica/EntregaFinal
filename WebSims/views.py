from django.shortcuts import render
from django.http import HttpResponse
from WebSims.models import Usuario, Modder, Mod
from WebSims.templates import *



def registrar_usuario(request):
    nombre_usuario="Eliza Pancakes"
    print("Registrando usuario")
    usuario=Usuario(nombre=nombre_usuario)
    usuario.save()
    respuesta=f"Usuario creado: {usuario.nombre}"
    return HttpResponse(respuesta)

def registrar_mod(request):
    nombre_mod="Wonderful Whims"
    creador_mod="TurboDriver"
    print("Registrando mod en la web")
    mod=Mod(nombre=nombre_mod, creador=creador_mod)
    mod.save()
    respuesta=f"Mod {mod.nombre}, creado por {mod.creador} cargado a la web."
    return HttpResponse(respuesta)

def listar_mods(request):
    mods=Mod.objects.all()
    respuesta=""
    for mod in mods:
        respuesta+=f"{mod.nombre} - {mod.creador}<br>" 
    return HttpResponse(respuesta)    
    
def listar_usuarios(request):
    usuarios=Usuario.objects.all()
    respuesta=""
    for usuario in usuarios:
        respuesta+=f"{usuario.nombre}<br>" 
    return HttpResponse(respuesta)    
    

def vista_inicio(request):
    return render(request, 'WebSims/inicio.html')

def vista_usuario(request):
    return render(request,"WebSims/Usuarios.html")

def vista_modder(request):
    return render(request,"WebSims/Modders.html")

def vista_mod(request):
    mods=Mod.objects.all()
    return render(request,"WebSims/Mods.html", {"mods":mods})
    






