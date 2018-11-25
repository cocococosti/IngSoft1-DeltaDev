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

	materias = Asignatura.objects.all()
	user = request.user

	if request.method == 'POST':

		if ((request.POST.get('modo')) == "Eliminar"):
			item = Asignatura.objects.filter(codigo = request.POST.get('item_id'))       
			item.delete()
			materias = Asignatura.objects.all()
		elif ((request.POST.get('modo')) == "Modificar"):
			return redirect('/modificar-asignatura/{}'.format(request.POST.get('item_id')))
		else:
			return render(request, 'Asignaturas/tablaAsignaturas.html', {'materias': materias})


	elif request.method=='GET':
		materias = Asignatura.objects.all()

	return render(request, 'Asignaturas/tablaAsignaturas.html', {'materias': materias})

def modificarAsignatura(request, codigo):
	"""Busca la materia en la base de datos y llena el formulario con los datos"""
	user = request.user
	materia = Asignatura.objects.get(codigo=codigo)
	if request.method == 'POST':
		form = RegistrarMatForm(user, request.POST, instance=materia)
		if form.is_valid():
			form.save()
			return redirect('/tabla-asignaturas/')
		else:
			return render(request, 'Asignaturas/modificarAsignatura.html', {'form':form})

	else:
		form = RegistrarMatForm(user,instance=materia)
		return render(request, 'Asignaturas/modificarAsignatura.html', {'form':form})

def registroAsignaturas(request):
	"""Genera el form para registro de asignaturas y guarda los datos en la base de datos."""

	user = request.user
	if request.method == 'POST':

		# Generamos el form
		form = RegistrarMatForm(user, request.POST)

		if form.is_valid():

			form.save()

			return redirect('/inicio/')
		else:
			return render(request, 'Asignaturas/registroAsignaturas.html', {'form':form})
	else:
		form = RegistrarMatForm(user)
		return render(request, 'Asignaturas/registroAsignaturas.html', {'form':form})
		
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
				# FALTA GUARDAR EL USUARIO EN profesor
				dept = Departamento.objects.filter(codigo=dpto).first()
				profesor = Profesor(
					user = User.objects.get(username=username),
					departamento = dept
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
