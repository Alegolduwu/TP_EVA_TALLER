from django.contrib import admin
from .models import alquiler, plataforma,videojuego,genero
# Register  your models here.

admin.site.register(alquiler)
admin.site.register(plataforma)
admin.site.register(videojuego)
admin.site.register(genero)