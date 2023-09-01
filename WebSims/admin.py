from django.contrib import admin
from .models import Usuario, Mod, Modder

admin.site.register(Usuario)
admin.site.register(Mod)
admin.site.register(Modder)