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

def home(request):
	return render(request,  'Asignaturas/home.html', {})
	

def tablaAsignaturas(request):
	"""Toma las asignaturas de la base de datos y las carga en la tabla."""

	materias = Asignatura.objects.all()

	if request.method == 'POST':

		if ((request.POST.get('modo')) == "Eliminar"):
			item = Asignatura.objects.filter(codigo = request.POST.get('item_id'))       
			item.delete()
			materias = Asignatura.objects.all()
		elif ((request.POST.get('modo')) == "Modificar"):
			materia = Asignatura.objects.filter(codigo = request.POST.get('item_id')).first()

			form = RegistrarMatForm(
				{"codigo"     : materia.codigo,
				"nombre"     : materia.nombre,
				"unidadesCredito"   : materia.unidadesCredito,
				"horasTeoria"              : materia.horasTeoria,
				"horasPractica" : materia.programa.horasPractica,
				"horasLab": materia.horasLab,
				"requisitos": materia.requisitos,
				"departamento"      : materia.departamento.codigo})

			return render(request, 'Asignaturas/modificarAsignatura.html', {'form':form})
		elif ((request.POST.get('boton')) == "Modificar"):

			form = RegistrarMatForm(request.POST)

			if form.is_valid():

				programa_id = Programa.objects.filter(nombre = form.cleaned_data['programa']).first()
				dpto_id = Departamento.objects.filter(codigo = form.cleaned_data['departamento']).first()
				area= Area.objects.filter(nombre = form.cleaned_data['area']).first()
				componente = Componente.objects.filter(nombre = form.cleaned_data['componente']).first()

				asignatura = Asignatura(
							codigo     = form.cleaned_data[ 'codigo' ].upper(),
							nombre     = form.cleaned_data['nombre'],
							unidadesCredito   = form.cleaned_data['unidadesCredito'],
							area              = area,
							programa = programa_id,
							departamento      = dpto_id,
							componente = componente)

				asignatura.save()

				materias = Asignatura.objects.all()
				return redirect('index/')
			else:
				return render(request, 'Asignaturas/tablaAsignaturas.html', {'materias': materias})


	elif request.method=='GET':
		materias = Asignatura.objects.all()

	return render(request, 'Asignaturas/tablaAsignaturas.html', {'materias': materias})


def registroAsignaturas(request):
	"""Genera el form para registro de asignaturas y guarda los datos en la base de datos."""

	if request.method == 'POST':

		# Generamos el form
		form = RegistrarMatForm(request.POST)

		if form.is_valid():

			#dpto_id = Departamento.objects.filter(codigo = form.cleaned_data['departamento']).first()
			
			asignatura = Asignatura(
						nombre     = form.cleaned_data['nombre'],
						codigo     = form.cleaned_data[ 'codigo' ].upper(),
						horasTeoria = form.cleaned_data['horasTeoria'],
						horasPractica = form.cleaned_data['horasPractica'],
						horasLab = form.cleaned_data['horasLab'],
						requisitos = form.cleaned_data['requisitos'],
						departamento = form.cleaned_data['departamento']
						)

			asignatura.save()

			return redirect('/inicio/')
		else:
			return render(request, 'Asignaturas/registroAsignaturas.html', {'form':form})
	else:
		form = RegistrarMatForm()
		return render(request, 'Asignaturas/registroAsignaturas.html', {'form':form})

	return render(request, 'Asignaturas/registroAsignaturas.html', {})
		
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