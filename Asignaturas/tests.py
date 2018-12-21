from django.test import TestCase, RequestFactory
from django.test import Client
from django.core.urlresolvers import reverse
from Asignaturas.models import *
from .forms import *
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import User
from django.contrib.auth.models import AnonymousUser
from django.db import IntegrityError	

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


# INICIO DE LAS PRUEBAS DE REGRESION


# Son pruebas ya efectuadas en sprints anteriores en el sistema
# que vuelven a ejecutarse para asegurarse de que se mantiene
# la funcionalidad del sistema


# CREATION OF MODELS
class AsignaturasTest(TestCase):

	# docstring para el departamento
	def create_departamento(self, codigo, nombre):
		return Departamento.objects.create(codigo=codigo, nombre=nombre)
		
	# docstring para la asignatura		
	def create_asignatura(self, codigo, nombre,uc, ht, hp, hl, d):
		return Asignatura.objects.create(codigo=codigo, nombre=nombre,unidadesCredito=uc, horasTeoria= ht, horasPractica=hp, horasLab=hl, departamento=d)

	# docstring para la disponibilidad
	def create_disponibilidad(self, bloque, dia):
		return Disponibilidad.objects.create(bloque=bloque, dia=dia)

	# docstring para la oferta
	def create_oferta(self, trimestre, profesor, materia, departamento):
		return OfertaDpto.objects.create(trimestre=trimestre, profesor=profesor, materia=materia, departamento=departamento)

	# do3cstring para los profesores
	def create_prof(self, nombre, apellido, email, cedula, departamento):
		return Profesor.objects.create(nombre=nombre, apellido=apellido, email=email, cedula=cedula, departamento=departamento)


	######## Pruebas frontera ########
	def test_codigo_asig_incorrecto_1(self):
		d = self.create_departamento("CI","Departamento de Computación y Tecnología de la Información")
		a = self.create_asignatura("CI-762", "Teoria de Algoritmos", 4, 4, 0, 0, d)
		form = RegistrarMatForm(user = User, instance = a)
		self.assertFalse(form.is_valid())

	def test_codigo_asig_incorrecto_2(self):
		d = self.create_departamento("CI","Departamento de Computación y Tecnología de la Información")
		a = self.create_asignatura("C8-7621", "Teoria de Algoritmos", 4, 4, 0, 0, d)
		form = RegistrarMatForm(user = User, instance = a)
		self.assertFalse(form.is_valid())

	def test_codigo_asig_incorrecto_3(self):
		d = self.create_departamento("CI","Departamento de Computación y Tecnología de la Información")
		a = self.create_asignatura("9I-7621", "Teoria de Algoritmos", 4, 4, 0, 0, d)
		form = RegistrarMatForm(user = User, instance = a)
		self.assertFalse(form.is_valid())

	def test_codigo_asig_incorrecto_4(self):
		d = self.create_departamento("CI","Departamento de Computación y Tecnología de la Información")
		a = self.create_asignatura("CIK7621", "Teoria de Algoritmos", 4, 4, 0, 0, d)
		form = RegistrarMatForm(user = User, instance = a)
		self.assertFalse(form.is_valid())

	def test_codigo_asig_incorrecto_5(self):
		d = self.create_departamento("CI","Departamento de Computación y Tecnología de la Información")
		a = self.create_asignatura("CI7621", "Teoria de Algoritmos", 4, 4, 0, 0, d)
		form = RegistrarMatForm(user = User, instance = a)
		self.assertFalse(form.is_valid())

	# Pruebas sobre los creditos	
	def test_creditos_asig_incorrecto_1(self):
		d = self.create_departamento("CI","Departamento de Computación y Tecnología de la Información")
		a = self.create_asignatura("CI-7621", "Teoria de Algoritmos", 0, 4, 0, 0, d)
		form = RegistrarMatForm(user = User, instance = a)
		self.assertFalse(form.is_valid())

	def test_horas_lab_incorrecta(self):
		d = self.create_departamento("CO","Departamento de Computo Cientifico")		
		a = self.create_asignatura("CO-5212","ANALISIS NUMERICO", 4, 6, 3, -1, d)
		form = RegistrarMatForm(user = User, instance = a)
		self.assertFalse(form.is_valid())

	def test_horas_practica_incorrecta(self):
		d = self.create_departamento("CO","Departamento de Computo Cientifico")		
		a = self.create_asignatura("CO-5212","ANALISIS NUMERICO", 4, 6, -1, 3, d)
		form = RegistrarMatForm(user = User, instance = a)
		self.assertFalse(form.is_valid())

	######## Pruebas de esquina ########

	def test_creditos_codigo_incorrecto(self):
		d = self.create_departamento("CI","Departamento de Computación y Tecnología de la Información")
		a = self.create_asignatura("CI7621", "Teoria de Algoritmos", 0, 4, 0, 0, d)
		form = RegistrarMatForm(user = User, instance = a)
		self.assertFalse(form.is_valid())

	def test_creditos_codigo_dpto_incorrecto(self):
		d = self.create_departamento("CO","Departamento de Computación y Tecnología de la Información")
		a = self.create_asignatura("CI7621", "Teoria de Algoritmos", 0, 4, 0, 0, d)
		form = RegistrarMatForm(user = User, instance = a)
		self.assertFalse(form.is_valid())

	def test_dpto_codigo_incorrecto(self):
		d = self.create_departamento("CI","Departamento de Computación y Tecnología de la Información")
		a = self.create_asignatura("CI7621", "Teoria de Algoritmos", 4, 4, 0, 0, d)
		form = RegistrarMatForm(user = User, instance = a)
		self.assertFalse(form.is_valid())

	def test_creditos_dpto_incorrecto(self):
		d = self.create_departamento("CO","Departamento de Computo Cientifico")
		a = self.create_asignatura("CI-7621", "Teoria de Algoritmos", 0, 4, 0, 0, d)
		form = RegistrarMatForm(user = User, instance = a)
		self.assertFalse(form.is_valid())



	######## Pruebas internas ########

	# Codigo y horas de laboratorio incorrectos
	def test_asignatura_incorrecta_1(self):
		d = self.create_departamento("CO","Departamento de Computo Cientifico")		
		a = self.create_asignatura("CI6319","MANEJO EN PREFERENCIAS EN BASE DE DATOS", 4, 6, 0, -1, d)
		form = RegistrarMatForm(user = User, instance = a)
		self.assertFalse(form.is_valid())

	# Codigo de diferente departamento, unidades de credito negativa
	def test_asignatura_incorrecta_2(self):
		d = self.create_departamento("CO","Departamento de Computo Cientifico")		
		a = self.create_asignatura("CI-6318","BASES DE DATOS HETEROGÉNEAS", -2, 6, 0, 3, d)
		form = RegistrarMatForm(user = User, instance = a)
		self.assertFalse(form.is_valid())

	# Codigo y horas de practica incorrectos
	def test_asignatura_incorrecta_3(self):
		d = self.create_departamento("CO","Departamento de Computo Cientifico")		
		a = self.create_asignatura("CI-73","WEB SEMÁNTICA I", 0, 6, -10, 3, d)
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
		a = self.create_asignatura("CO-5212","ANALISIS NUMERICO", 4, 6, 3, 3, d)
		self.assertTrue(isinstance(a, Asignatura))
		self.assertEqual(a.__str__(), "CO-5212 Nombre: ANALISIS NUMERICO Dpto: CO UC: 4")


	# Creacion de asignatura con un departamento al que no pertenece
	def test_asignatura_distinto_dpto(self):

		dpto = self.create_departamento("CI","Departamento de Computación y Tecnología de la Información")
		asignatura = self.create_asignatura("CO-5211", "CONTROL DE PROYECTOS DE PROGRAMAS", 4, 4, 0, 0, dpto)
		self.assertFalse(asignatura.codigo == dpto.codigo)



class ProfesorTest(TestCase):

	# Metodo para crear valores iniciales por defecto
	# en los casos de prueba
	def setUp(self):

		d_compu = Departamento.objects.create(nombre="Departamento de Matematicas", codigo="MA")
		
		Profesor.objects.create(nombre="Constanza", apellido="Abarca", email="cocosti@gmail.com", cedula="V-24.343.542", departamento=d_compu)
		Profesor.objects.create(nombre="Pedro", apellido="Maldonado", email="pmaldonado@usb.ve", cedula="V-25.777.898", departamento=d_compu)


	# docstring para el departamento
	def create_departamento(self, codigo, nombre):
		return Departamento.objects.create(codigo=codigo, nombre=nombre)
		
	# docstring para la asignatura		
	def create_asignatura(self, codigo, nombre,uc, ht, hp, hl, d):
		return Asignatura.objects.create(codigo=codigo, nombre=nombre,unidadesCredito=uc, horasTeoria= ht, horasPractica=hp, horasLab=hl , departamento=d)

	# docstring para la disponibilidad
	def create_disponibilidad(self, bloque, dia):
		return Disponibilidad.objects.create(bloque=bloque, dia=dia)

	# docstring para la oferta
	def create_oferta(self, trimestre, profesor, materia, departamento):
		return OfertaDpto.objects.create(trimestre=trimestre, profesor=profesor, materia=materia, departamento=departamento)

	# do3cstring para los profesores
	def create_prof(self, nombre, apellido, email, cedula, departamento):
		return Profesor.objects.create(nombre=nombre, apellido=apellido, email=email, cedula=cedula, departamento=departamento)


	# Prueba del nombre de un profesor en la base de datos
	def test_nombre_profesor(self):

		profesor = Profesor.objects.get(cedula="V-24.343.542")
		self.assertEqual(profesor.nombre + " " + profesor.apellido, "Constanza Abarca")

	# Prueba de error al registrar un profesor ya existente
	def test_profesor_existente(self):

		d_compu = Departamento.objects.get(codigo="MA")
		with self.assertRaises(IntegrityError):
			Profesor.objects.create(nombre="Luis", apellido="Maldonado", email="pmaldonado@usb.ve", cedula="V-25.777.898", departamento=d_compu)

	# Prueba de creacion de un profesor
	def test_creacion_profesor(self):

		dpto = Departamento.objects.get(codigo="MA")
		profesor = self.create_prof("Luis", "Marcano", "marcano@hotmail.com", "V-14.421.214", departamento=dpto)
		self.assertEqual(profesor.nombre + " " + profesor.apellido + " " + profesor.cedula, "Luis Marcano V-14.421.214")


	# Prueba de busqueda de profesor
	def test_profesor_con_departamento_existente(self):

		d = self.create_departamento("CO","Departamento de Computo Cientifico")
		d2 = Departamento.objects.get(codigo="MA") 
		asignatura = self.create_asignatura("CO-5212","ANALISIS NUMERICO", 4, 6, 3, 3, d)
		profesor = Profesor.objects.get(cedula="V-24.343.542")

		profesor2 = Profesor.objects.filter(departamento=d2).first()

		self.assertEqual(profesor.nombre, profesor2.nombre)
 

	# Prueba de error al intentar crear un departamento ya existente
	def test_dpto_existente(self): 

		with self.assertRaises(IntegrityError):
			depto = Departamento.objects.create(nombre="Departamento de Matematicas", codigo="MA")

	# Prueba de error al intentar crear un departamento ya existente
	def test_dpto_existente_2(self):
	
		d = self.create_departamento("CO","Departamento de Computo Cientifico")

		with self.assertRaises(IntegrityError):
			d2 = self.create_departamento("CO", "Departamento de Computo Cientifico")
		
		
"""
 class OfertaTest(TestCase):

 	# Metodo para crear valores iniciales por defecto
 	# en los casos de prueba

 	def setUp(self):

 		d_compu = Departamento.objects.create(nombre="Departamento de Matematicas", codigo="MA")
		
 		Profesor.objects.create(nombre="Constanza", apellido="Abarca", email="cocosti@gmail.com", cedula="V-24.343.542", departamento=d_compu)
 		Profesor.objects.create(nombre="Pedro", apellido="Maldonado", email="pmaldonado@usb.ve", cedula="V-25.777.898", departamento=d_compu)

 		a = self.create_asignatura("MA-6939", "DISEÑO Y ANALISIS DE EXPERIMENTOS", 4, 4, 0, 0, "", d_compu)
 

 	# docstring para el departamento
 	def create_departamento(self, codigo, nombre):
 		return Departamento.objects.create(codigo=codigo, nombre=nombre)
		
 	# docstring para la asignatura		
 	def create_asignatura(self, codigo, nombre,uc, ht, hp, hl, d):
 		return Asignatura.objects.create(codigo=codigo, nombre=nombre,unidadesCredito=uc, horasTeoria= ht, horasPractica=hp, horasLab=hl, departamento=d)

 	# docstring para la disponibilidad
 	def create_disponibilidad(self, bloque, dia):
 		return Disponibilidad.objects.create(bloque=bloque, dia=dia)

 	# docstring para la oferta
 	def create_oferta(self, profesor, materia, departamento):
 		return OfertaDpto.objects.create(profesor=profesor, materia=materia, departamento=departamento)

 	# do3cstring para los profesores
 	def create_prof(self, nombre, apellido, email, cedula, departamento):
 		return Profesor.objects.create(nombre=nombre, apellido=apellido, email=email, cedula=cedula, departamento=departamento)


 	# Prueba de creacion de disponibilidad
 	def test_disponibilidad_1(self):
 		disponibilidad = self.create_disponibilidad(bloque=4,dia=2)
 		self.assertEqual(disponibilidad.__str__(), "Martes, bloque 4")

 	# Prueba de creacion de disponibilidad
 	def test_disponibilidad_2(self):
 		disponibilidad = self.create_disponibilidad(bloque=10,dia=4)
 		self.assertEqual(disponibilidad.__str__(), str(disponibilidad.get_dia_display()) + ", bloque " + str(disponibilidad.bloque))

 	# Prueba de creacion de oferta trimestral
 	def test_oferta_1(self):
 		d = self.create_departamento("CI","Departamento de Computación y Tecnología de la Información")
 		a = self.create_asignatura("CI-7621", "Teoria de Algoritmos", 4, 4, 0, 0, d)
 		p = self.create_prof("María", "Ramirez", "12-10042@usb.ve", "V-25.766.738", d)
 		p.asignaturas.add(a)
 		oferta = OfertaDpto.objects.create(profesor=p, materia=a, departamento=d)
 		self.assertEqual(oferta.__str__(), "AJ-19, "+str(oferta.profesor_id)+", CI-7621")

 	# Prueba de creacion de oferta trimestral
 	def test_oferta_2(self):
 		dpto = Departamento.objects.get(codigo="MA")
 		asignatura = Asignatura.objects.get(codigo="MA-6939")
 		asignatura2 = self.create_asignatura("MA-5273", "COMBINATORIA", 4, 4, 0, 0, dpto)
 		profesor = Profesor.objects.get(cedula="V-25.777.898")

 		profesor.asignaturas.add(asignatura2)
 		oferta = OfertaDpto.objects.create(profesor=profesor, materia=asignatura2, departamento=dpto)
 		self.assertEqual(oferta.__str__(), "AJ-19, "+str(oferta.profesor_id)+", MA-5273")

 	# Prueba de creacion de oferta trimestral
 	def test_oferta_3(self):

 		dpto = self.create_departamento("CI","Departamento de Computación y Tecnología de la Información")
 		asignatura = self.create_asignatura("CI-5211", "CONTROL DE PROYECTOS DE PROGRAMAS", 4, 4, 0, 0, dpto)
 		profesor = Profesor.objects.get(cedula="V-25.777.898")

 		profesor.asignaturas.add(asignatura)
 		oferta = OfertaDpto.objects.create(profesor=profesor, materia=asignatura, departamento=dpto)
 		self.assertEqual(oferta.__str__(), oferta.trimestre + ", "+ str(oferta.profesor_id) + ", " + oferta.materia_id)

"""