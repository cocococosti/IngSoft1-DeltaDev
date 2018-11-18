from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from Asignaturas.models import *
from .forms import *


def inicio(request):
	"""Carga la página incial."""

	return render(request, 'Asignaturas/index.html', {})

def home(request):
	return render(request,  'Asignaturas/home.html', {})

def login(request):
	return render(request,  'Asignaturas/login.html', {})		

def tablaAsignaturas(request):
	"""Toma las asignaturas de la base de datos y las carga en la tabla."""

	materias = Asignatura.objects.all()

	if request.method == 'POST':

		if ((request.POST.get('modo')) == "Eliminar"):
			item = Asignatura.objects.filter(codigo = request.POST.get('item_id'))       
			item.delete()
			materias = Asignatura.objects.all()
		elif ((request.POST.get('modo')) == "Modificar"):
			materia = Asignatura.objects.filter(codigo = request.POST.get('item_id'))[0]

			form = RegistrarMatForm(
				{"codigo"     : materia.codigo,
				"nombre"     : materia.nombre,
				"unidadesCredito"   : materia.unidadesCredito,
				"area"              : materia.area,
				"programa" : materia.programa.nombre,
				"departamento"      : materia.departamento.codigo,
				"componente": materia.componente.nombre})

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
			return redirect('/inicio/')
		else:
			return render(request, 'Asignaturas/registroAsignaturas.html', {'form':form})
	else:
		form = RegistrarMatForm()
		return render(request, 'Asignaturas/registroAsignaturas.html', {'form':form})
		
def signup(request):
	"""Registro de un usuario."""
	
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('asignaturas/')
	else:
		form = UserCreationForm()
	return render(request, 'Asignaturas/signup.html', {'form': form})