from django.db import models

class Familia(models.Model):

    nombre = models.CharField(max_length=40)
    dni = models.IntegerField()
    nacionalidad = models.CharField(max_length=40)
