from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

# Modelos de cada Tabla y sus atributos

class Departamento(models.Model):
	codigo = models.CharField(primary_key=True, max_length=3)
	nombre = models.CharField(max_length=60, unique=True)

class Profesor(models.Model):
	user = models.OneToOneField(User, default="", on_delete=models.CASCADE)
	departamento = models.ForeignKey(Departamento, default="",on_delete=models.CASCADE)
	

class Asignatura(models.Model):
	codigo = models.CharField(primary_key=True,max_length=7, validators=[RegexValidator(regex='^[A-Z]{2}-[0-9]{4}$', message = 'Codigo Invalido')])
	nombre = models.CharField(max_length=60)
	unidadesCredito = models.IntegerField()  
	horasTeoria = models.IntegerField()
	horasPractica = models.IntegerField()
	horasLab = models.IntegerField()
	requisitos = models.ManyToManyField("self", blank=True)
	departamento = models.ForeignKey(Departamento, default="",on_delete=models.CASCADE)
