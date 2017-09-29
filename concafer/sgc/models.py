# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


# Create your models here.

# Modelos: Propietario, Recolector, Cooperativa

class Recolector(models.Model):
    nombre = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Propietario(models.Model):
    nombre = models.CharField(max_length=20)
    contrasena = models.CharField(max_length=20)
    nombreFinca = models.CharField(max_length=20)

class AdminCooperativa(models.Model):
    nombre = models.CharField(max_length=20)
    contrasena = models.CharField(max_length=20)

class Superusuario(models.Model):
    nombre = models.CharField(max_length=20)
    contrasena = models.CharField(max_length=20)

class SuperNumerario(models.Model):
    nombre = models.CharField(max_length=20)
    contrasena = models.CharField(max_length=20)


