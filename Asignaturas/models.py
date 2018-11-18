from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _


# Modelos de cada Tabla y sus atributos

class Departamento(models.Model):
    codigo = models.CharField(primary_key=True, max_length=15)
    nombre = models.CharField(max_length=60, unique=True)

class Asignatura(models.Model):
    codigo = models.CharField(primary_key=True,max_length=7, validators=[RegexValidator(regex='^[A-Z]{2}-[0-9]{4}$', message = 'Codigo Invalido')])
    nombre = models.CharField(max_length=60)
    unidadesCredito = models.IntegerField()  
    horasTeoria = models.IntegerField()
    horasPractica = models.IntegerField()
    horasLab = models.IntegerField()
    requisitos =  ArrayField(models.CharField(max_length=200))
    departamento = models.ForeignKey(Departamento, default="",on_delete=models.CASCADE)
