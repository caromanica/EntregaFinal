from django.db import models


class Usuario(models.Model):
    nombre=models.CharField(max_length=50)
    usuario=models.CharField(max_length=30)
    email=models.EmailField()


class Modder(models.Model):
    usuario= models.CharField(max_length=30)
    website= models.URLField()
    email= models.EmailField()

class Mod(models.Model):
    nombre=models.CharField(max_length=50)
    creador=models.CharField(max_length=30)
    
