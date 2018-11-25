from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.core.validators import *

# Modelos de cada Tabla y sus atributos

class Departamento(models.Model):
	""" Tabla Departamento la cual posee el codigo del departamento como 
		clave primaria y y a su vez posee sus respectivas validaciones para verificar
		que los datos de entrada se encuentran en el dominio."""

	codigo = models.CharField(primary_key=True, max_length=2, validators=[MaxLengthValidator(2, message='El código del Departamento debe contener exactamente 2 caracteres'), MinLengthValidator(2, message='El código del Departamento debe contener exactamente 2 caracteres')])
	nombre = models.CharField(max_length=60, unique=True, validators=[MaxLengthValidator(60, message='El nombre del Departamento a lo sumo puede contener 60 caracteres'), MinLengthValidator(1, message='El nombre de la asignatura debe ser mayor a un caracter')])

	#Permite ingresar los elementos a la tabla Departamento ordenados por su codigo
	class Meta:
		ordering = ["codigo"]

	# metodo que permite devolver la informacion del Departamento
	def __str__(self):
		return self.codigo + ": " + self.nombre

class Profesor(models.Model):
	""" Tabla profesor en la cual se almacena la informacion basica de usuario por defecto de Django
		y el departento al cual pertece el profesor mediante la clave foranea."""

	user = models.OneToOneField(User, default="", on_delete=models.CASCADE)
	departamento = models.ForeignKey(Departamento, default="",on_delete=models.CASCADE)
	

class Asignatura(models.Model):
	""" Tabla asignatura con sus respectivos atributos y validaciones del dominio de entrada."""
	
	codigo = models.CharField(primary_key=True,max_length=7, validators=[RegexValidator(regex='^[A-Z]{2}-[0-9]{4}$', message = 'El código de la asignatura es inválido'), MaxLengthValidator(7, message='El código de la asignatura debe contener exactamente 7 caracteres'), MinLengthValidator(7, message='El código de la asignatura debe contener exactamente 7 caracteres')])
	nombre = models.CharField(max_length=60, validators=[MaxLengthValidator(60, message='El nombre de la asignatura a lo sumo puede contener 60 caracteres'), MinLengthValidator(1, message='El nombre de la asignatura debe contener al menos un caracter')])
	unidadesCredito = models.IntegerField(default=0,validators=[MinValueValidator(1, message='La asignatura debe contener al menos una unidad de crédito')])  
	horasTeoria = models.IntegerField(default=0, validators=[MinValueValidator(0, message='Las horas de teoría no pueden ser negativas')])
	horasPractica = models.IntegerField(default=0,validators=[MinValueValidator(0, message='Las horas de practica no pueden ser negativas')])
	horasLab = models.IntegerField(default=0, validators=[MinValueValidator(0, message='Las horas de laboratorio no pueden ser negativas')])
	requisitos = models.ManyToManyField("self", symmetrical=False, blank=True)
	departamento = models.ForeignKey(Departamento, default="",on_delete=models.CASCADE)

	#Permite ingresar los elementos a la tabla asignatura ordenados por su codigo
	class Meta:
		ordering = ["codigo"]

	# metodo que permite devolver la informacion de la asignatura
	def __str__(self):
		return self.codigo + " Nombre: " + self.nombre + " Dpto: " + self.departamento_id + " UC: " + str(self.unidadesCredito)
