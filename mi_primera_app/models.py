from django.db import models
from unittest.util import _MAX_LENGTH

class Familia(models.Model):

    nombre = models.CharField(max_length=40)
    dni = models.IntegerField()
    nacionalidad = models.CharField(max_length=40)

class Automoviles(models.Model):

    tipo = models.CharField(max_length=40)
    marca = models.CharField(max_length=40)
    anoxx = models.IntegerField()

class Longevidad_animales(models.Model):
    animal = models.CharField(max_length=40)
    longevidad = models.IntegerField()
