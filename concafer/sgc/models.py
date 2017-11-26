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

class Empleado(models.Model):
    OCUPACIONES=(
        ('Admin de finca', 'Admin de finca'),
        ('Labores con el café', 'Labores con el café'),
        ('Labores con el cacao', 'Labores con el cacao'),
        ('Labores con el maíz', 'Labores con el maíz'),
        ('Labores con el plátano', 'Labores con el plátano'),
    )

    MUNICIPIOS=(
        ('Pereira', 'Pereira'),
        ('Dosquebradas', 'Dosquebradas'),
        ('Santa Rosa de Cabal', 'Santa Rosa de Cabal'),
        ('Marsella', 'Marsella'),
        ('La Virginia', 'La Virginia'),
    )

    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    cedula = models.IntegerField()
    celular = models.IntegerField()
    municipio = models.CharField(max_length=20)
    ocupacion = models.CharField(max_length=20)

    #municipio = models.CharField(max_length=100, choices=MUNICIPIOS)
    #ocupacion = models.CharField(max_length=100, choices=OCUPACIONES)

    def __str__(self):
        return self.nombre

class Cotizacion(models.Model):
    nombre_de_la_finca = models.CharField(max_length=30)
    telefono = models.IntegerField()
    municipio = models.CharField(max_length=20)
    cantidad_de_dias_por_semana = models.IntegerField()
    cantidad_de_horas_por_dia = models.IntegerField()

    def __str__(self):
        return self.nombre_de_la_finca




