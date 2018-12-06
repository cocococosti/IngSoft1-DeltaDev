from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from Asignaturas.models import *
from .forms import *
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import logout
from django.http import HttpResponse


def inicio(request):
	"""Carga la página incial."""

	return render(request, 'Asignaturas/index.html', {})


def tablaAsignaturas(request):
	"""Toma las asignaturas de la base de datos y las carga en la tabla."""

	user = request.user
	prof = Profesor.objects.get(user = user)
	dept = prof.departamento.codigo

	materias = Asignatura.objects.filter(departamento = dept).all()
	
	if request.method == 'POST':

		if ((request.POST.get('modo')) == "Eliminar"):

			item = Asignatura.objects.filter(codigo = request.POST.get('item_id')) 
			if (Asignatura.objects.filter(codigo = request.POST.get('item_id')).first() != None):  
				itemAsig = Asignatura.objects.filter(codigo = request.POST.get('item_id')).first().departamento.codigo
				# Chequeamos si el usuario autentica es del mismo dpto que desea eliminar
				prof = Profesor.objects.get(user = user)
				dept = prof.departamento.codigo
				if (dept == itemAsig):
					item.delete()
					materias = Asignatura.objects.filter(departamento = dept).all()

		elif ((request.POST.get('modo')) == "Modificar"):
			item = Asignatura.objects.filter(codigo = request.POST.get('item_id')) 
			if (Asignatura.objects.filter(codigo = request.POST.get('item_id')).first() != None):  
				itemAsig = Asignatura.objects.filter(codigo = request.POST.get('item_id')).first().departamento.codigo
				# Chequeamos si el usuario autentica es del mismo dpto que desea eliminar
				prof = Profesor.objects.get(user = user)
				dept = prof.departamento.codigo
				if (dept == itemAsig):

					return redirect('/modificar-asignatura/{}'.format(request.POST.get('item_id')))

		else:
			return render(request, 'Asignaturas/tablaAsignaturas.html', {'materias': materias})


	elif request.method=='GET':
		materias = Asignatura.objects.filter(departamento = dept).all()

	return render(request, 'Asignaturas/tablaAsignaturas.html', {'materias': materias})

def modificarAsignatura(request, codigo):
	"""Busca la materia en la base de datos y llena el formulario con los datos"""
	user = request.user
	prof = Profesor.objects.get(user = user)
	dept = prof.departamento.codigo
	materia = Asignatura.objects.get(codigo=codigo)
	if request.method == 'POST':
		form = RegistrarMatForm(user, request.POST, instance=materia)
		if form.is_valid():
			codigo = form.cleaned_data['codigo'][0]+form.cleaned_data['codigo'][1]

			if (codigo == dept):
				form.save()
				return redirect('/tabla-asignaturas/')
			else:
				return render(request, 'Asignaturas/modificarAsignatura.html', {'form':form})
		else:
			return render(request, 'Asignaturas/modificarAsignatura.html', {'form':form})

	else:
		form = RegistrarMatForm(user,instance=materia)
		return render(request, 'Asignaturas/modificarAsignatura.html', {'form':form})

def registroAsignaturas(request):
	"""Genera el form para registro de asignaturas y guarda los datos en la base de datos."""

	user = request.user
	prof = Profesor.objects.get(user = user)
	dept = prof.departamento.codigo
	if request.method == 'POST':

		# Generamos el form
		form = RegistrarMatForm(user, request.POST)

		if form.is_valid():
			codigo = form.cleaned_data['codigo'][0]+form.cleaned_data['codigo'][1]

			if (codigo == dept):

				form.save()

				return redirect('/inicio/')
			else:
				return render(request, 'Asignaturas/registroAsignaturas.html', {'form':form})
		else:
			return render(request, 'Asignaturas/registroAsignaturas.html', {'form':form})
	else:
		form = RegistrarMatForm(user)
		return render(request, 'Asignaturas/registroAsignaturas.html', {'form':form})

def tablaProfesores(request):
	"""Toma las asignaturas de la base de datos y las carga en la tabla."""

	user = request.user
	prof = Profesor.objects.get(user = user)
	dept = prof.departamento.codigo

	profesores = Profesor.objects.filter(departamento = dept).exclude(cedula=prof.cedula)
	
	if request.method == 'POST':

		if ((request.POST.get('modo')) == "Eliminar"):

			item = Profesor.objects.filter(cedula = request.POST.get('item_id')) 
			if (Profesor.objects.filter(cedula = request.POST.get('item_id')).first() != None):  
				itemProf = Profesor.objects.filter(cedula = request.POST.get('item_id')).first().departamento.codigo
				# Chequeamos si el usuario autentica es del mismo dpto que desea eliminar
				prof = Profesor.objects.get(user = user)
				dept = prof.departamento.codigo
				if (dept == itemProf):
					item.delete()
					profesores = Profesor.objects.filter(departamento = dept).exclude(cedula=prof.cedula)

		elif ((request.POST.get('modo')) == "Modificar"):
			item = Profesor.objects.filter(cedula = request.POST.get('item_id')) 
			if (Profesor.objects.filter(cedula = request.POST.get('item_id')).first() != None):  
				itemProf = Profesor.objects.filter(cedula = request.POST.get('item_id')).first().departamento.codigo
				# Chequeamos si el usuario autentica es del mismo dpto que desea eliminar
				prof = Profesor.objects.get(user = user)
				dept = prof.departamento.codigo
				if (dept == itemProf):

					return redirect('/modificar-profesor/{}'.format(request.POST.get('item_id')))

		else:
			return render(request, 'Asignaturas/tablaProfesores.html', {'profesores': profesores})


	return render(request, 'Asignaturas/tablaProfesores.html', {'profesores': profesores})

def registroProfesores(request):
	
	user = request.user
	prof = Profesor.objects.get(user = user)
	dept = prof.departamento.codigo
	if request.method == 'POST':

		# Generamos el form
		form = RegistrarProfForm(user, request.POST)

		if form.is_valid():
			codigo = form.cleaned_data['departamento'].codigo

			if (codigo == dept):

				form.save()

				return redirect('/inicio/')
			else:
				return render(request, 'Asignaturas/registroProfesor.html', {'form':form})
		else:
			return render(request, 'Asignaturas/registroProfesor.html', {'form':form})
	else:
		form = RegistrarProfForm(user)
		return render(request, 'Asignaturas/registroProfesor.html', {'form':form})

def modificarProfesor(request, codigo):
	"""Busca la materia en la base de datos y llena el formulario con los datos"""
	user = request.user
	prof = Profesor.objects.get(user = user)
	dept = prof.departamento.codigo
	profesor = Profesor.objects.get(cedula=codigo)

	if request.method == 'POST':
		form = RegistrarProfForm(user, request.POST, instance=profesor)
		if form.is_valid():
			codigo = form.cleaned_data['departamento'].codigo

			if (codigo == dept):
				form.save()
				return redirect('/tabla-profesores/')
			else:
				return render(request, 'Asignaturas/modificarProfesor.html', {'form':form})
		else:
			return render(request, 'Asignaturas/modificarProfesor.html', {'form':form})

	else:
		form = RegistrarProfForm(user,instance=profesor)
		return render(request, 'Asignaturas/modificarProfesor.html', {'form':form})


def tablaOferta(request):
	user = request.user
	prof = Profesor.objects.get(user = user)
	dept = prof.departamento
	profesores = Profesor.objects.filter(departamento = dept.codigo).all()
	materias = Asignatura.objects.filter(departamento = dept.codigo).all()
	if request.method == 'POST':

		if ((request.POST.get('modo')) == "Eliminar"):
			item = Oferta.objects.filter(id = request.POST.get('item_id')).first()
			if (item != None):
				if (dept.codigo == item.profesor.departamento.codigo):
					item.delete()
		elif ((request.POST.get('modo')) == "Modificar"):
			return redirect('/modificar-oferta/{}'.format(request.POST.get('item_id')))
		else:
			profs = request.POST.getlist('profesores_oferta')
			asig = Asignatura.objects.filter(codigo = request.POST.get('asignatura')).first()
			for cedula in profs:
				p =  Profesor.objects.filter(cedula = cedula).first()
				oferta = Oferta(
					trimestre = "SD-18",
					profesor = p,
					materia = asig,
					departamento = dept)
				oferta.save()


	ofertas = Oferta.objects.filter(departamento = dept).all()
	return render(request, 'Asignaturas/tablaOferta.html', {'departamento':dept, 'materias':materias, 'profesores':profesores, 'ofertas':ofertas})

def modificarOferta(request, id):
	oferta = Oferta.objects.filter(id = id).first()
	user = request.user
	prof = Profesor.objects.get(user = user)
	dept = prof.departamento
	profesores = Profesor.objects.filter(departamento = dept.codigo).all()
	if request.method == 'POST':
		oferta.profesor = Profesor.objects.get(cedula = request.POST.get('cedula'))
		oferta.save()
		return redirect('/tabla-oferta/')

	return render(request, 'Asignaturas/modificarOferta.html', {'oferta':oferta, 'profesores': profesores})


def autenticacion(request):
	"""Registro de un usuario."""
	
	form = SignUpForm()
	form2 = AuthForm()

	return render(request, 'Asignaturas/login.html', {'form': form, 'form2':form2})

def registrar(request):

	if request.method == 'POST':
			form = SignUpForm(request.POST)
			if form.is_valid():
				form.save()
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
	logout(request)

	return redirect('/autenticacion/')
