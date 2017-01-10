from django.conf.urls import url
from django.contrib import admin
from elecciones import views
from elecciones.views import *
from elecciones import models

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^$', views.menuPrincipal, name="Menu Principal" ),
    url(r'^login/', views.Login, name="Loguearse" ),
    url(r'^crearCircunscrito/', crearCircunscrito.as_view(), name="Aniadir un nuevo circunscrito" ),
    url(r'^listarCircunscritos/', listarCircunscritos.as_view(), name="Listar todos los circunscritos" ),
    url(r'^circunscritos/(?P<circunscrito_id>\d+)', detalleCirc.as_view(), name='Detalle circuns'),
]
