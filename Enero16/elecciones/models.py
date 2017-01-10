from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.

class Circunscripcion(models.Model):
    nombre=models.CharField(max_length=100)
    escanios=models.IntegerField()
    def get_absolute_url(self):
        return reverse('author-detail', kwargs={'pk': self.pk})
        def __unicode__(self):
            return (self.nombre)

class Mesa (models.Model):
    nombre=models.CharField(max_length=100)
    votos=models.IntegerField()
    circunscripcion=models.ForeignKey(Circunscripcion)
    def __unicode__(self):
        return (self.nombre)


class Partido (models.Model):
    nombre=models.CharField(max_length=100)
    votos=models.IntegerField()
    mesa=models.ForeignKey(Mesa)
    def __unicode__(self):
        return (self.nombre)

class Resultado (models.Model):
    partido=models.OneToOneField(Partido)
    mesa=models.OneToOneField(Mesa)
    votos=models.IntegerField()
