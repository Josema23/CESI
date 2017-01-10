from django.contrib import admin

from .models import Jugador, Equipo, Partido, Jornada

# Register your models here.

#Hacemos nuestros modelos visibles en la pagina del administrador

admin.site.register(Jugador)
admin.site.register(Equipo)
admin.site.register(Partido)
admin.site.register(Jornada)
