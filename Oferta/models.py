from django.db import models
from IngSoft1-DeltaDev.Asignaturas.models import *
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.core.validators import *

# Create your models here.
class Profesor(models.Model):
	""" Tabla profesor en la cual se almacena la informacion basica de usuario por defecto de Django
		y el departento al cual pertece el profesor mediante la clave foranea."""

	user = models.OneToOneField(User, default="", on_delete=models.CASCADE)
	departamento = models.ForeignKey(Departamento, default="",on_delete=models.CASCADE)
	nombre = models.CharField(max_length=50, default="")
	apellido = models.CharField(max_length=50, default="")
	email = models.EmailField(max_length=200, default="")
	cedula = models.CharField(max_length=12, unique=True, default="")
	disponibilidad = models.ManyToManyField('Disponibilidad', blank=True)
	asignaturas = models.ManyToManyField('Asignatura', blank=True)

	class Meta:
		"""Provee algunas configuraciones básicas con respecto a las operaciones del modelo."""
        # Ordenamiento por defecto: según su cédula
		ordering = ["cedula"]

	def __str__(self):
		"""Muestra la instancia de Profesor como nombre apellido """
		return self.nombre + " " + self.apellido	

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