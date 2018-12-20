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
	jefe = models.ForeignKey('Profesor', related_name="jefe_de", null=True, on_delete=models.SET_NULL)

	#Permite ingresar los elementos a la tabla Departamento ordenados por su codigo
	class Meta:
		ordering = ["codigo"]

	# metodo que permite devolver la informacion del Departamento
	def __str__(self):
		return self.codigo + ": " + self.nombre

		def nombre_corto(self):
			"""
			Retorna el nombre del Departamento sin la frase inicial
			'Departamento de'.
			"""

			nombre = str(self)

			if nombre.startswith("Departamento de "):
				nombre = nombre[16:]

			return nombre

	def tiene_jefe(self):
		"""
		Determina si un Departamento tiene un jefe asociado.
		"""

		return bool(self.jefe)

	def jefe_coherente(self):
		"""
		Determina si el jefe del Departamento tiene coherencia
		con su Departamento asociado, es decir, que un jefe pertenezca
		al mismo Departamento que dirige.
		"""

		if not self.tiene_jefe():
			raise ValueError(
				"No se puede verificar la coherencia en la jefatura de un Departamento sin jefe."
			)

		return self.jefe.departamento == self


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

class Profesor(models.Model):
	"""
	Modelo que representa un profesor de la USB
	incluye su nombre, apellido, cedula, email, disponibilidad semanal, departamento
	y las asignaturas que puede dar.
	"""

	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	cedula = models.CharField(max_length=12, unique=True)
	disponibilidad = models.ManyToManyField('Disponibilidad', blank=True)
	departamento = models.ForeignKey('Departamento')
	email = models.EmailField(max_length=200)
	asignaturas = models.ManyToManyField('Asignatura', blank=True)
	user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)

	class Meta:
		"""
		Provee algunas configuraciones básicas con respecto a las
		operaciones del modelo.
		"""

		# Ordenamiento por defecto: según su cédula
		ordering = ["cedula"]

	def __str__(self):
		"""
		Muestra la instancia de Profesor como
		nombre apellido
		"""
		return self.nombre + " " + self.apellido

class Oferta(models.Model):
	''' Tabla que representa las asignaturas que cada profesor puede dar en la proxima
		oferta (asignaturas por confirmar)'''
	trimestre = models.CharField(max_length=5, default="SD-18", validators=[MaxLengthValidator(5, message='La específicación del trimestre son máximo 5 letras'), MinLengthValidator(5, message='La específicación del trimestre son mínimo 5 letras')])
	profesor = models.ForeignKey('Profesor', default="",on_delete=models.CASCADE, blank=True, null=True)
	materia = models.ForeignKey('Asignatura', default="",on_delete=models.CASCADE)
	preferencia = models.NullBooleanField(default=None)
	departamento = models.ForeignKey('Departamento',  default="",on_delete=models.CASCADE)

	class Meta:
		"""
		Provee algunas configuraciones básicas con respecto a las
		operaciones del modelo.
		"""

		# Ordenamiento por defecto por trimestre
		ordering = ["trimestre"]
		# Limita a que no hayan repeticiones de la tupla trimestre-profesor-materia
		# Garantiza que no aparezca 2 o mas veces un mismo profesor dando una misma materia en un mismo trimestre
		unique_together = ("trimestre","profesor", "materia")

	def __str__(self):
		"""
		Muestra la oferta de manera abreviada
		"""
		return self.trimestre + ", "+ str(self.profesor_id) + ", " + self.materia_id + ", " + str(self.preferencia)

class OfertaFinal(models.Model):
	""" Tabla que representa las asignaturas que cada profesor va a dar en la proxima
		oferta """
	trimestre = models.CharField(max_length=5, default="SD-18", validators=[MaxLengthValidator(5, message='La específicación del trimestre son máximo 5 letras'), MinLengthValidator(5, message='La específicación del trimestre son mínimo 5 letras')])
	profesor = models.ForeignKey('Profesor', default="",on_delete=models.CASCADE, blank=True, null=True)
	materia = models.ForeignKey('Asignatura', default="",on_delete=models.CASCADE)
	departamento = models.ForeignKey('Departamento',  default="",on_delete=models.CASCADE)
	horario = models.CharField(max_length=15, default="", validators=[MaxLengthValidator(15, message='El campo de horario puede contener hasta 15 letras'), MinLengthValidator(3, message='El horario debe contener al menos 3 letras')])

	class Meta:
		"""
		Provee algunas configuraciones básicas con respecto a las
		operaciones del modelo.
		"""

		# Ordenamiento por defecto por trimestre
		ordering = ["trimestre"]
		# Limita a que no hayan repeticiones de la tupla trimestre-profesor-materia
		# Garantiza que no aparezca 2 o mas veces un mismo profesor dando una misma materia en un mismo trimestre
		unique_together = ("trimestre","profesor", "materia")

	def __str__(self):
		"""
		Muestra la oferta de manera abreviada
		"""
		return self.trimestre + ", "+ str(self.profesor_id) + ", " + self.materia_id 

class Disponibilidad(models.Model):
	"""
	Modelo auxiliar que representa un horario (día, bloque) de
	disponibilidad para un profesor.
	"""

	LUNES = (1, 'Lunes')
	MARTES = (2, 'Martes')
	MIERCOLES = (3, 'Miércoles')
	JUEVES = (4, 'Jueves')
	VIERNES = (5, 'Viernes')
	SABADO = (6, 'Sábado')

	DIA_CHOICES = (
		LUNES,
		MARTES,
		MIERCOLES,
		JUEVES,
		VIERNES,
		SABADO
	)

	bloque = models.IntegerField(
		validators=[
			MaxValueValidator(12),
			MinValueValidator(1)
		]
	)
	dia = models.IntegerField(
		choices=DIA_CHOICES,
		validators=[
			MaxValueValidator(6),
			MinValueValidator(1)
		]
	)

	class Meta:
		"""
		Provee algunas configuraciones básicas con respecto a las
		operaciones del modelo.
		"""

		# Ordenamiento por defecto: según el día, y luego según el bloque
		ordering = ["dia", "bloque"]

	def identificador_unico(self):
		"""
		Retorna el identificador único numérico del bloque (dia y hora)
		según una formula biyectiva de R² a R.
		"""

		cantidad_bloques = 12

		return cantidad_bloques*(self.dia-1) + self.bloque

	def matriz_bloques():
		"""
		Devuelve un diccionario que contiene los valores por biyección
		asignados a cada bloque, cada valor representando un día,
		de modo que se pueda representar fácilmente la matriz de manera
		visual.
		"""

		matriz_bloques = {
			1: [1, 13, 25, 36, 49, 61],
			2: [2, 14, 26, 38, 50, 62],
			3: [3, 15, 27, 39, 51, 63],
			4: [4, 16, 28, 40, 52, 64],
			5: [5, 17, 29, 41, 53, 65],
			6: [6, 18, 30, 42, 54, 66],
			7: [7, 19, 31, 43, 55, 67],
			8: [8, 20, 32, 44, 56, 68],
			9: [9, 21, 33, 45, 57, 69],
			10: [10, 22, 34, 46, 58, 70],
			11: [11, 23, 35, 47, 59, 71],
			12: [12, 24, 36, 48, 60, 72],
		}

		return matriz_bloques

	def __str__(self):
		"""
		Muestra representación en cadena de caracteres del bloque de disponibilidad,
		indicando su día y luego su bloque.
		"""

		return self.get_dia_display() + ", bloque " + str(self.bloque)