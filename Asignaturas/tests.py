from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse
from Asignaturas.models import *
from .forms import *
from django.contrib.auth.base_user import BaseUserManager

# Fronteras:

# * El codigo de las asignaturas debe cumplir:
# - Debe tener exactamente 7 caracteres
# - Los dos primeros caracteres son letras
# - El tercer caracter debe ser un guion
# - El resto de caracteres deben ser numeros del 0 al 9
#
# * Los creditos de la asignatura deben ser minimo 1
#
# * Las horas de teoria deben ser minimo 4
#
# * Las horas de practica deben ser minimo 0
#
# * Las horas de laboratorio deben ser minimo 0
#
# * El codigo del departamento debe contener exactamente 2 caracteres



# models test

# CREATION OF MODELS
class AsignaturasTest(TestCase):

	# docstring for DepartamentoTest
	def create_departamento(self, codigo, nombre):
		return Departamento.objects.create(codigo=codigo, nombre=nombre)
		
	# docstring for Asignatura		
	def create_asignatura(self, codigo, nombre,uc, ht, hp, hl, r, d):
		return Asignatura.objects.create(codigo=codigo, nombre=nombre,unidadesCredito=uc, horasTeoria= ht, horasPractica=hp, horasLab=hl, requisitos=r, departamento=d)

	######## Pruebas frontera ########
	def test_codigo_asig_incorrecto_1(self):
		d = self.create_departamento("CI","Departamento de Computación y Tecnología de la Información")
		a = self.create_asignatura("CI-762", "Teoria de Algoritmos", 4, 4, 0, 0, "", d)
		form = RegistrarMatForm(user = User, instance = a)
		self.assertFalse(form.is_valid())

	def test_codigo_asig_incorrecto_2(self):
		d = self.create_departamento("CI","Departamento de Computación y Tecnología de la Información")
		a = self.create_asignatura("C8-7621", "Teoria de Algoritmos", 4, 4, 0, 0, "", d)
		form = RegistrarMatForm(user = User, instance = a)
		self.assertFalse(form.is_valid())

	def test_codigo_asig_incorrecto_3(self):
		d = self.create_departamento("CI","Departamento de Computación y Tecnología de la Información")
		a = self.create_asignatura("9I-7621", "Teoria de Algoritmos", 4, 4, 0, 0, "", d)
		form = RegistrarMatForm(user = User, instance = a)
		self.assertFalse(form.is_valid())

	def test_codigo_asig_incorrecto_4(self):
		d = self.create_departamento("CI","Departamento de Computación y Tecnología de la Información")
		a = self.create_asignatura("CIK7621", "Teoria de Algoritmos", 4, 4, 0, 0, "", d)
		form = RegistrarMatForm(user = User, instance = a)
		self.assertFalse(form.is_valid())

	def test_codigo_asig_incorrecto_5(self):
		d = self.create_departamento("CI","Departamento de Computación y Tecnología de la Información")
		a = self.create_asignatura("CI7621", "Teoria de Algoritmos", 4, 4, 0, 0, "", d)
		form = RegistrarMatForm(user = User, instance = a)
		self.assertFalse(form.is_valid())

	# Pruebas sobre los creditos	
	def test_creditos_asig_incorrecto_1(self):
		d = self.create_departamento("CI","Departamento de Computación y Tecnología de la Información")
		a = self.create_asignatura("CI-7621", "Teoria de Algoritmos", 0, 4, 0, 0, "", d)
		form = RegistrarMatForm(user = User, instance = a)
		self.assertFalse(form.is_valid())

	def test_horas_lab_incorrecta(self):
		d = self.create_departamento("CO","Departamento de Computo Cientifico")		
		a = self.create_asignatura("CO-5212","ANALISIS NUMERICO", 4, 6, 3, -1, "", d)
		form = RegistrarMatForm(user = User, instance = a)
		self.assertFalse(form.is_valid())

	def test_horas_practica_incorrecta(self):
		d = self.create_departamento("CO","Departamento de Computo Cientifico")		
		a = self.create_asignatura("CO-5212","ANALISIS NUMERICO", 4, 6, -1, 3, "", d)
		form = RegistrarMatForm(user = User, instance = a)
		self.assertFalse(form.is_valid())

	######## Pruebas de esquina ########

	def test_creditos_codigo_incorrecto(self):
		d = self.create_departamento("CI","Departamento de Computación y Tecnología de la Información")
		a = self.create_asignatura("CI7621", "Teoria de Algoritmos", 0, 4, 0, 0, "", d)
		form = RegistrarMatForm(user = User, instance = a)
		self.assertFalse(form.is_valid())

	def test_creditos_codigo_dpto_incorrecto(self):
		d = self.create_departamento("CO","Departamento de Computación y Tecnología de la Información")
		a = self.create_asignatura("CI7621", "Teoria de Algoritmos", 0, 4, 0, 0, "", d)
		form = RegistrarMatForm(user = User, instance = a)
		self.assertFalse(form.is_valid())

	def test_dpto_codigo_incorrecto(self):
		d = self.create_departamento("CI","Departamento de Computación y Tecnología de la Información")
		a = self.create_asignatura("CI7621", "Teoria de Algoritmos", 4, 4, 0, 0, "", d)
		form = RegistrarMatForm(user = User, instance = a)
		self.assertFalse(form.is_valid())

	def test_creditos_dpto_incorrecto(self):
		d = self.create_departamento("CO","Departamento de Computo Cientifico")
		a = self.create_asignatura("CI-7621", "Teoria de Algoritmos", 0, 4, 0, 0, "", d)
		form = RegistrarMatForm(user = User, instance = a)
		self.assertFalse(form.is_valid())



	######## Pruebas internas ########

	# Codigo y horas de laboratorio incorrectos
	def test_asignatura_incorrecta_1(self):
		d = self.create_departamento("CO","Departamento de Computo Cientifico")		
		a = self.create_asignatura("CI6319","MANEJO EN PREFERENCIAS EN BASE DE DATOS", 4, 6, 0, -1, "", d)
		form = RegistrarMatForm(user = User, instance = a)
		self.assertFalse(form.is_valid())

	# Codigo de diferente departamento, unidades de credito negativa
	def test_asignatura_incorrecta_2(self):
		d = self.create_departamento("CO","Departamento de Computo Cientifico")		
		a = self.create_asignatura("CI-6318","BASES DE DATOS HETEROGÉNEAS", -2, 6, 0, 3, "", d)
		form = RegistrarMatForm(user = User, instance = a)
		self.assertFalse(form.is_valid())

	# Codigo y horas de practica incorrectos
	def test_asignatura_incorrecta_3(self):
		d = self.create_departamento("CO","Departamento de Computo Cientifico")		
		a = self.create_asignatura("CI-73","WEB SEMÁNTICA I", 0, 6, -10, 3, "", d)
		form = RegistrarMatForm(user = User, instance = a)
		self.assertFalse(form.is_valid())

	# Prueba de creacion de departamento
	def test_creacion_departamento(self):
		d = self.create_departamento("CI","Departamento de Computación y Tecnología de la Información")
		self.assertTrue(isinstance(d,Departamento))		
		self.assertEqual(d.__str__(), "CI: Departamento de Computación y Tecnología de la Información")

	# Prueba de creacion de asignatura
	def test_creacion_asignatura(self):		
		d = self.create_departamento("CO","Departamento de Computo Cientifico")		
		a = self.create_asignatura("CO-5212","ANALISIS NUMERICO", 4, 6, 3, 3, "", d)
		self.assertTrue(isinstance(a, Asignatura))
		self.assertEqual(a.__str__(), "CO-5212 Nombre: ANALISIS NUMERICO Dpto: CO UC: 4")