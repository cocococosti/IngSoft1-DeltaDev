from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
from django.contrib.postgres.fields import ArrayField

# Modelos de cada Tabla y sus atributos

class Departamento(models.Model):
    codigo = models.CharField(primary_key=True, max_length=2)
    nombre = models.CharField(max_length=60, unique=True)
    jefe = models.ForeignKey('Profesor', related_name="Jefe_del", blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
    	ordering = ["codigo"]

    def __str__(self):
    	return self.codigo + ": " + self.nombre

class Profesor(models.Model):
	cedulaIdentidad = models.IntegerField(primary_key=True)
	primerNombre = models.CharField(max_length=12)
	segundoNombre = models.CharField(max_length=12, blank=True, default="")
	primerApellido = models.CharField(max_length=12)
	segundoApellido = models.CharField(max_length=12)
	correo = models.EmailField(max_length=320)
	departamento = models.ForeignKey('Departamento', default="",on_delete=models.CASCADE)

	class Meta:
		ordering = ["cedulaIdentidad"]

	def __str__(self):
		return self.primerNombre + " " + self.segundoNombre+ " " + self.primerApellido + " " +self.segundoApellido + ",Dpto: " +self.departamento_id

class Asignatura(models.Model):
    codigo = models.CharField(primary_key=True,max_length=7, validators=[RegexValidator(regex='^[A-Z]{2}-[0-9]{4}$', message = 'Codigo Invalido')])
    nombre = models.CharField(max_length=60)
    unidadesCredito = models.IntegerField(default=0)  
    horasTeoria = models.IntegerField(default=0)
    horasPractica = models.IntegerField(default=0)
    horasLab = models.IntegerField(default=0)
    departamento = models.ForeignKey('Departamento', on_delete=models.CASCADE)
    
    class Meta:
    	ordering = ["codigo"]

    def __str__(self):
    	return self.codigo + " Nombre: " + self.nombre + " Dpto: " + self.departamento_id + " UC: " + str(self.unidadesCredito)

class Requisito(models.Model):
	
	asignatura = models.ForeignKey('Asignatura', on_delete=models.CASCADE)
	requiere = models.ForeignKey('Asignatura', related_name="es_necesario",on_delete=models.CASCADE)

	class Meta:
		ordering = ["asignatura"]

	def __str__(self): 
		return self.asignatura_id + " Requiere " + self.requiere_id