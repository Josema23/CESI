from django.db import models
from django.utils import timezone

#definicion del Modelo (objeto) Equipo
#models.Model -> Hace que Equipo sea un modelo de Django, indicando que debe ser guardado en la Base de Datos

class Equipo(models.Model):
    nombreEquipo=models.CharField(max_length=50)
    ciudad=models.CharField(max_length=50)
    creacion=models.DateField()
    historia=models.CharField(max_length=1000)
    entrenador=models.CharField(max_length=50)
    escudo=models.ImageField()
    estadio=models.CharField(max_length=50)
    puntos=models.IntegerField(default=0)
    golesAfavor=models.IntegerField(default=0)
    golesenContra=models.IntegerField(default=0)
    partidosJugados=models.IntegerField(default=0)
    partidosGanados=models.IntegerField(default=0)
    partidosPerdidos=models.IntegerField(default=0)
    partidosEmpatados=models.IntegerField(default=0)
    def __unicode__ (self):
        return self.nombreEquipo

class Jugador(models.Model):
    nombre=models.CharField(max_length=50)
    nombrecompleto=models.CharField(max_length=50)
    edad=models.IntegerField(default=0)
    imagen=models.ImageField()
    equipo=models.ForeignKey(Equipo)            #ForeignKey() -> Vinculo con otro modelo (En este caso con Equipo)
    dorsal=models.IntegerField(default=0)
    nacimiento=models.DateField()
    goles=models.IntegerField(default=0)
    asistencias=models.IntegerField(default=0)
    amarillas=models.IntegerField(default=0)
    rojas=models.IntegerField(default=0)
    delantero="Delantero"
    centrocampista="Centrocampista"
    defensa="Defensa"
    portero="Portero"
    posiciones=((delantero, 'Delantero'), (centrocampista, 'Centrocampista'), (defensa, 'Defensa'), (portero, 'Portero'))
    posicion=models.CharField(max_length=30, choices=posiciones)
    def __unicode__(self):
        return self.nombre

class Jornada(models.Model):

    numJornada=models.IntegerField(default=0)
    def __unicode__(self):
        return unicode (self.numJornada)


class Partido(models.Model):
    jornada=models.ForeignKey(Jornada)
    estadio=models.CharField(max_length=50)
    equipoLocal=models.ForeignKey(Equipo, related_name='Local')
    equipoVisitante=models.ForeignKey(Equipo, related_name='Visitante')
    resultado=models.CharField(max_length=15)
    fecha=models.DateField()
    enJuego="En juego"
    finalizado="Finalizado"
    sinComenzar="Sin comenzar"
    estados=((enJuego, 'En juego'), (finalizado, 'Finalizado'), (sinComenzar,'Sin comenzar'))
    estado=models.CharField(max_length=50, choices=estados)
    def __unicode__(self):
        return self.equipoLocal.nombreEquipo+"-"+self.equipoVisitante.nombreEquipo
