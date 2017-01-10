"""LigaSantander URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from Liga import views
from Liga.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    url(r'^$', views.menuPrincipal, name='Menu principal'),

    url(r'^registro/', views.usuarioRegistro, name='Signup'),   #Registro de un usuario
    url(r'^login/', views.usuarioLogin, name="Login"),          #Login de un usuario ya registrado
	url(r'^logout/', views.usuarioLogout, name="Logout"),      #desconexion de un usuario previamente conectado

    url(r'^equipos/crearequipo/$', views.crearEquipo, name='crearEquipo'),
    url(r'^equipo/(?P<equipo_id>\d+)/modificar/$', views.modEquipo, name='Modificar Equipo'),
    url(r'^equipo/(?P<equipo_id>\d+)/borrar/$', views.borrarEquipo, name='Eliminar Equipo'),

    url(r'^equipo/(?P<equipo_id>\d+)$', views.mostrarEquipo, name='Ver equipo'),  #Mostrar un equipo deseado
    url(r'^equipo/(?P<equipo_id>\d+)/crearJugador/$', views.crearJugador, name='Crear Jugador'),
    url(r'^equipo/(?P<equipo_id>\d+)/mostrarJugador/(?P<jugador_id>\d+)/$', views.mostrarJugador, name='Mostrar Jugador'),

    url(r'^equipo/(?P<equipo_id>\d+)/mostrarJugador/(?P<jugador_id>\d+)/modificar/$', views.modificarJugador, name='Modificar Jugador'),
    url(r'^equipo/(?P<equipo_id>\d+)/mostrarJugador/(?P<jugador_id>\d+)/borrar/$', views.borrarJugador, name='Eliminar Jugador'),


    url(r'^equipo/(?P<equipo_id>\d+)/plantilla/$', views.listarPlantilla, name='Listar Plantilla'),


    url(r'^jornada/(?P<jornada_id>\d+)/crearpartidos/$', views.crearPartido, name='Crear Partido'),

    url(r'^jornada/(?P<jornada_id>\d+)/modificar/$', views.modNumJornada, name='Modificar Numero Jornada'),
    url(r'^jornada/(?P<jornada_id>\d+)/modificarPartido/$', views.modificarPartido, name='Modificar Numero Jornada'),

    url(r'^equipos/crear/$', views.crearEquipo, name='Crear Equipo'),  #Muestra todos los equipos de la Liga

    url(r'^calendario/crearjornada/$', views.crearJornada, name='Anyadir una Jornada'),  #Muestra el calendario de jornadas
    url(r'^jornada/(?P<jornada_id>\d+)/borrarjornada/$', views.borrarJornada, name='Eliminar una Jornada'),


    url(r'^clasificacion/$', views.clasificacion, name='Mostrar Clasificacion'), #Muestra la clasificacion actual
    url(r'^equipos/$', views.listarEquipos, name='Listar Equipos'),  #Muestra todos los equipos de la Liga
    url(r'^calendario/$', views.calendario, name='Mostrar Calendario'),  #Muestra el calendario de jornadas
    url(r'^jornada/(?P<jornada_id>\d+)/$', views.mostrarJornada, name='Mostrar Jornada'),  #Muestra la jornada actual


    url(r'^admin/', admin.site.urls),       #administrador

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
