from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django import forms
from django.http import HttpResponse
from django.core.mail import send_mass_mail
from django.template.loader import render_to_string
from django.urls import reverse

from Asignaturas.models import *
from .forms import *

def inicio(request):
	"""Carga la página incial."""
	return render(request, 'Asignaturas/index.html', {})


def tablaAsignaturas(request):
	"""Toma las asignaturas de la base de datos y las carga en la tabla."""

	# Obtenemos usuario autenticado 
	user = request.user

	# Obtenemos profesor que corresponde al usuario
	prof = Profesor.objects.get(user = user)

	# Obtenemos codigo del dpto del profesor
	dept = prof.departamento.codigo

	# Obtenemos todas las materias del dpto
	materias = Asignatura.objects.filter(departamento = dept).all()

	# Si se recibe una solicitud POST desde el template
	if request.method == 'POST':

		# En el template si se selecciona el boton "Eliminar" se envia la variable
		# modo con el valor "Eliminar". De esta manera podemos saber que acción tomar
		# dependiendo del boton que se seleccione.
		if ((request.POST.get('modo')) == "Eliminar"):

			# Obtenemos la asignatura a eliminar de la base de datos (el
			# codigo de la materia se obtiene de la vista)
			item = Asignatura.objects.filter(codigo = request.POST.get('item_id'))
			
			# Chequear que la asignatura existe
			if (Asignatura.objects.filter(codigo = request.POST.get('item_id')).first() != None):
				
				# Obtenemos codigo del dpto al que pertenece la asignatura
				itemAsig = Asignatura.objects.filter(codigo = request.POST.get('item_id')).first().departamento.codigo
				
				# Chequeamos si el usuario autenticado es del mismo dpto que el de la
				# asignatura que se desea eliminar
				prof = Profesor.objects.get(user = user)

				# Si el codigo del dept del user autenticado es el mismo que el de la asignatura
				if (dept == itemAsig):

					# Eliminar materia de la base
					item.delete()

					# Obtenemos todas las asignaturas nuevamente (sin la que eliminamos)
					materias = Asignatura.objects.filter(departamento = dept).all()
		
		# Si se selecciono el boton modificar
		elif ((request.POST.get('modo')) == "Modificar"):

			# Obtener materia a modificar
			item = Asignatura.objects.filter(codigo = request.POST.get('item_id'))
			
			# Si la materia existe
			if (Asignatura.objects.filter(codigo = request.POST.get('item_id')).first() != None):
				
				# Codigo del dpto al que pertenece la materia
				itemAsig = Asignatura.objects.filter(codigo = request.POST.get('item_id')).first().departamento.codigo
				
				# Chequeamos si el usuario autenticado es del mismo dpto que desea eliminar
				prof = Profesor.objects.get(user = user)

				# Si la materia es del mismo dpto que el jefe
				if (dept == itemAsig):

					# Redireccionar al template de modificar la materia
					return redirect('/modificar-asignatura/{}'.format(request.POST.get('item_id')))

	# Carga la lista de asignaturas
	return render(request, 'Asignaturas/tablaAsignaturas.html', {'materias': materias})

def modificarAsignatura(request, codigo):
	"""Busca la materia en la base de datos y llena el formulario con los datos"""

	# Usuario autenticado
	user = request.user

	# Profesor que corresponde al usuario
	prof = Profesor.objects.get(user = user)

	# Codigo del dpto del profesor
	dept = prof.departamento.codigo

	# Materia a modificar
	materia = Asignatura.objects.get(codigo=codigo)

	# Guardamos materia otra vez (lo necesitamos despues)
	materia2 = Asignatura.objects.get(codigo=codigo)
	
	if request.method == 'POST':

		# Obtenemos datos de los campos del form
		form = RegistrarMatForm(user, request.POST, instance=materia)

		# Si los campos del form son validos
		if form.is_valid():

			# codigo de la materia original
			c = codigo
			
			# Obtenemos codigo del dpto del form
			codigo = form.cleaned_data['codigo'][0]+form.cleaned_data['codigo'][1]
				
			# Si el codigo del formulario es el mismo que el dpto del usuario registrado
			if (codigo == dept):

				# Obtenemos codigo completo de la materia
				codMateria = form.cleaned_data['codigo']

				# si se esta modificando el codigo de la maetria
				if (codMateria != c):
					# Eliminar la materia con el codigo viejo
					materia2.delete()

				# Guardamos datos del form en la base de datos
				form.save()

				# Redireccionamos a la tabla de asignaturas
				return redirect('/tabla-asignaturas/')

			else:

				# Si el codigo es invalido continuamos en la misma pagina
				return render(request, 'Asignaturas/modificarAsignatura.html', {'form':form})
		
		else:

			# Si el form es invalido continuamos en la misma pagina
			return render(request, 'Asignaturas/modificarAsignatura.html', {'form':form})

	else:

		# Cargar el form
		form = RegistrarMatForm(user,instance=materia)

		# Cargamos pagina con el form
		return render(request, 'Asignaturas/modificarAsignatura.html', {'form':form})


def registroAsignaturas(request):
	"""Genera el form para registro de asignaturas y guarda los datos en la base de datos."""
	
	# Obtenemos usuario registrado
	user = request.user

	# Obtenemos profesor
	prof = Profesor.objects.get(user = user)

	# Obtenemos codigo del dpto
	dept = prof.departamento.codigo

	if request.method == 'POST':

		# Leemos campos del template
		form = RegistrarMatForm(user, request.POST)

		# Si el form es valido
		if form.is_valid():

			# Obtenemos codigo
			codigo = form.cleaned_data['codigo'][0]+form.cleaned_data['codigo'][1]

			# Si el dpto de la materia es el mismo que el del profesor
			if (codigo == dept):

				form.save()

				# Redireccionamos al inicio
				return redirect('/inicio/')

			else:
				return render(request, 'Asignaturas/registroAsignaturas.html', {'form':form})
		else:
			return render(request, 'Asignaturas/registroAsignaturas.html', {'form':form})
	else:

		# Cargar form vavio
		form = RegistrarMatForm(user)
		return render(request, 'Asignaturas/registroAsignaturas.html', {'form':form})

def tablaProfesores(request):
	"""Toma las asignaturas de la base de datos y las carga en la tabla."""

	# Obtenemos usuario autenticado
	user = request.user

	# Obtenemos profesor
	prof = Profesor.objects.get(user = user)

	# Codigo del dpto
	dept = prof.departamento.codigo

	# Obtenemos todos los profesores del dpto
	profesores = Profesor.objects.filter(departamento = dept).exclude(cedula=prof.cedula)

	if request.method == 'POST':

		# En el template si se selecciona el boton "Eliminar" se envia la variable
		# modo con el valor "Eliminar". De esta manera podemos saber que acción tomar
		# dependiendo del boton que se seleccione.
		if ((request.POST.get('modo')) == "Eliminar"):

			# Obtenemos profesor a eliminar
			item = Profesor.objects.filter(cedula = request.POST.get('item_id'))
			
			# Si el profesor existe
			if (Profesor.objects.filter(cedula = request.POST.get('item_id')).first() != None):
				
				itemProf = Profesor.objects.filter(cedula = request.POST.get('item_id')).first().departamento.codigo
				

				# Si el prof a eliminar es del mismo dpto del user autenticado
				if (dept == itemProf):
					
					# Eliminar profesor
					item.delete()
					profesores = Profesor.objects.filter(departamento = dept).exclude(cedula=prof.cedula)

		# Si se selecciona el boton modificar			
		elif ((request.POST.get('modo')) == "Modificar"):

			# Profesor a modificar
			item = Profesor.objects.filter(cedula = request.POST.get('item_id'))
			
			# si el profesor existe
			if (Profesor.objects.filter(cedula = request.POST.get('item_id')).first() != None):
				
				# Obtenemos el profesor de la base de datos usando ci enviada por el template
				itemProf = Profesor.objects.filter(cedula = request.POST.get('item_id')).first().departamento.codigo
				
				# si el dpto del prof a eliminar es el mismo del jefe
				if (dept == itemProf):

					# redireccionar a la pagina de modificar
					return redirect('/modificar-profesor/{}'.format(request.POST.get('item_id')))

		
	# Cargar tabla de profesores
	return render(request, 'Asignaturas/tablaProfesores.html', {'profesores': profesores})

def registroProfesores(request):
	""" Registra un profesor en la base de datos. """

	# Usuario autenticado
	user = request.user

	# Profesor que corresponde al usuario
	prof = Profesor.objects.get(user = user)
	
	# Dpto al que pertenece el profesor
	dept = prof.departamento.codigo
	
	# Si se recibe una solicitud post
	if request.method == 'POST':

		# Leemos campos del form de profesor
		form = RegistrarProfForm(user, request.POST)

		# Si los campos del form son validos
		if form.is_valid():

			# Obtenemos codigo del dpto del prof a registrar
			codigo = form.cleaned_data['departamento'].codigo

			# Si el profesor pertenece al dpto del jefe
			if (codigo == dept):

				# Guardamos datos del profesor en la base de datos
				form.save()

				# Redireccionamos a la pagina de inicio
				return redirect('/inicio/')
	else:

		# Generamos form vacio
		form = RegistrarProfForm(user)
		
		# Cargamos pagina de registro
		return render(request, 'Asignaturas/registroProfesor.html', {'form':form})

def seleccionMatProfesores(request, ci):
	""" Guarda las preferencia del profesor segun la oferta de asignatura enviada """
	
	# Usuario autenticado
	user = request.user

	# Profesor que corresponde al usuario
	prof = Profesor.objects.get(cedula=ci)

	# Dpto del profesor
	dept = prof.departamento.codigo
	
	# obtener materias a las que el prof fue asignado
	oferta_prof = [oferta_asig for oferta_asig in Oferta.objects.filter(profesor__cedula=ci)]
	
	if request.method == 'POST':

		# Leer datos del form
		form = PreferenciaForm(oferta_prof, request.POST)
		
		if form.is_valid():
			
			# Obtenemos preferencias seleccionadas del template
			preferencias = request.POST.getlist('preferencias')
			
			# De las materias a las que el prof fue asignado
			for oferta_asig in oferta_prof:

				# si el profesor las escogio en el template
				if oferta_asig.materia.codigo in preferencias:
					
					# preferencia de la asignatura es cierta,
					# usamos este booleano para saber si marcar al prof
					# rojo en la oferta
					oferta_asig.preferencia = True

					# guardar en a base de datos
					oferta_asig.save()

			return redirect('/inicio/')
		
		else :
			return render(request, 'Asignaturas/dictaProfesor.html', {'form': form})
	else:

		# Cargar form de preferencias
		form = PreferenciaForm(oferta_prof)
		return render(request, 'Asignaturas/dictaProfesor.html', {'form':form})

def modificarProfesor(request, codigo):
	"""Busca el profesor en la base de datos y llena el formulario con los datos"""
	
	user = request.user
	prof = Profesor.objects.get(user = user)
	dept = prof.departamento.codigo
	profesor = Profesor.objects.get(cedula=codigo)

	if request.method == 'POST':
		
		# Cargar form con los datos de la base de datos
		form = RegistrarProfForm(user, request.POST, instance=profesor)
		
		if form.is_valid():
			
			# codigo del dptp
			codigo = form.cleaned_data['departamento'].codigo

			# si el dpto de jefe es el mismo de la materia a modificar
			if (codigo == dept):

				# guardar datos
				form.save()

				return redirect('/tabla-profesores/')
			
			else:
				return render(request, 'Asignaturas/modificarProfesor.html', {'form':form})
		else:
			return render(request, 'Asignaturas/modificarProfesor.html', {'form':form})

	else:

		# Cargar form con datos ya llenos
		form = RegistrarProfForm(user,instance=profesor)
		return render(request, 'Asignaturas/modificarProfesor.html', {'form':form})


def tablaOferta(request):
	""" Muestra la oferta de asignaturas """
	
	# usuario autenticado
	user = request.user
	# profesor que corresponde al usuario
	prof = Profesor.objects.get(user=user)
	# dpto del prof autenticado
	dept = prof.departamento
	# los profesores del dpto
	profesores = Profesor.objects.filter(departamento = dept.codigo).all()
	# las maerias del dpto
	materias = Asignatura.objects.filter(departamento = dept.codigo).all()
	
	if request.method == 'POST':

		# si se selecciona boton eliminar
		if ((request.POST.get('modo')) == "Eliminar"):
			
			# obtenemos oferta seleccionada
			item = Oferta.objects.filter(id = request.POST.get('item_id')).first()
			
			# si la oferta existe
			if (item != None):

				# si la oferta es del dpto del jefe
				if (item.profesor==None):
					item.delete()
				elif (dept.codigo == item.profesor.departamento.codigo):
					
					item.delete()
		
		# si se selecciona modificar, redireccionar a la pagina de modificar
		elif ((request.POST.get('modo')) == "Modificar"):
			return redirect('/modificar-oferta/{}'.format(request.POST.get('item_id')))
		
		# si se selecciona enviar oferta
		elif request.POST.get('enviar_oferta'):
			
			# enviar correo
			profs = {'h':'MAIL'}
			ofertas = Oferta.objects.filter(departamento = dept).all()
			send_email(user, request)

			# cargar tabla de ofertas
			return render(request, 'Asignaturas/tablaOferta.html', {'departamento':dept, 'materias':materias, 'profesores':profesores, 'ofertas':ofertas, 'pro':profs})
		
		# si se selecciona agregar oferta
		else:

			# Asignatura de la oferta
			asig = Asignatura.objects.get(codigo=request.POST.get('asignatura'))
			# Profesores que expresaron preferencia por la asignatura
			profesores = asig.profesor_set.all()
			# guardar oferta para cada profesor

			# si no se registraron profesores para esa materia
			if (len(profesores)==0):
				# se registra la oferta con None en el campo profesor
				Oferta.objects.create(
						trimestre = "SD-18",
						materia=asig,
						departamento=dept)
			else:
				for profesor in profesores:
					# registrar oferta para cada profesor
					try:
						Oferta.objects.create(
								trimestre = "SD-18",
								profesor=profesor,
								materia=asig,
								departamento=dept)
					except:
						pass

	# cargar tabla de ofertas
	ofertas = Oferta.objects.filter(departamento = dept).all()
	return render(request, 'Asignaturas/tablaOferta.html', {'departamento':dept, 'materias':materias, 'profesores':profesores, 'ofertas':ofertas})

def modificarOferta(request, id):
	""" Carga form de una oferta con los datos ya guardados. """

	# Obtenemos la oferta a modificar
	oferta = Oferta.objects.filter(id = id).first()
	user = request.user
	prof = Profesor.objects.get(user = user)
	dept = prof.departamento
	profesores = Profesor.objects.filter(departamento = dept.codigo).all()
	
	if request.method == 'POST':
		
		# De una oferta solo modificamos el profesor asignado
		oferta.profesor = Profesor.objects.get(cedula = request.POST.get('cedula'))
		oferta.save()
		
		return redirect('/tabla-oferta/')

	return render(request, 'Asignaturas/modificarOferta.html', {'oferta':oferta, 'profesores': profesores})


def autenticacion(request):
	"""Manejo de registro o autenticacion de un usuario."""
	
	form = SignUpForm()
	form2 = AuthForm()

	return render(request, 'Asignaturas/login.html', {'form': form, 'form2':form2})

def registrar(request):
	""" Regostro de usuario """

	if request.method == 'POST':

			# Cargamos el form
			form = SignUpForm(request.POST)
			
			if form.is_valid():
				# Guardamos form en tabla de users
				form.save()

				# Guardamos el profesor
				username = form.cleaned_data.get('username')
				dpto = form.cleaned_data.get('departamento')
				dept = Departamento.objects.filter(codigo=dpto).first()
				nombre = form.cleaned_data.get('nombre')
				apellido = form.cleaned_data.get('apellido')
				cedula = form.cleaned_data.get('cedula')

				profesor = Profesor(
					nombre = nombre,
					apellido = apellido,
					user = User.objects.get(username=username),
					departamento = dept,
					cedula = cedula
					)
				profesor.save()
	return redirect('/autenticacion/')

def entrar(request):
	""" Acceder al sistema """

	if request.method == 'POST':
		form = AuthForm(data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect ('/inicio/')
	return redirect('/autenticacion/')


def salir(request):
	""" Salir del sistema """
	logout(request)
	return redirect('/autenticacion/')

def send_email(jefe, request):
	""" Formato del correo a enviar """

	# Ofertas de asignaturas a las que fue asignado el profesor
	ofertas = Oferta.objects.order_by('profesor_id')

	# Lista de profesores
	prof_list = {}

	# Para cada oferta
	for oferta in ofertas:
		# Agregar maeria a la lista de materias que el profesor ha sido asignado
		prof_list.setdefault(oferta.profesor, []).append(oferta.materia.nombre)

	# Lista de datos de correos a enviar
	correos = []

	# Para cada profesor y sus materias asignadas
	for profesor, materias in prof_list.items():
		if (profesor==None):
			pass
		else:
			# Obtener link a enviar al profesor
			relative_url = reverse('preferencias', args=(profesor.cedula,))
			full_url = request.build_absolute_uri(relative_url)
			# full_url = request.get_full_path(relative_url)
			mensaje_txt = render_to_string('email.txt', {'materias': ", ".join(materias), 'enlace': full_url})
			
			# Atributos del correo a enviar
			correo = (
					'Materias para dictar el proximo trimestre',
					mensaje_txt,
					jefe.email,
					[profesor.email],
					)
			correos.append(correo)
		
	# Enviar todos los correos
	send_mass_mail(correos,fail_silently=False)
