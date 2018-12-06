from django.core.validators import RegexValidator
from Asignaturas.models import *
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm

class RegistrarMatForm(ModelForm):
	def __init__(self, user, *args, **kwargs):
		super(RegistrarMatForm, self).__init__(*args, **kwargs)
		self.user = user
		if kwargs and kwargs['instance']:
			materia = kwargs['instance']
			self.fields['requisitos'].queryset =\
					Asignatura.objects.exclude(codigo=materia.codigo)
		if not self.user.is_anonymous:
			departamento =\
					Profesor.objects.get(user=self.user).departamento
			self.fields['departamento'].queryset =\
					Departamento.objects.filter(codigo=departamento.codigo)
	class Meta():
		model = Asignatura
		fields = ['codigo', 'nombre', 'unidadesCredito',
		'horasTeoria', 'horasPractica', 'horasLab', 'requisitos', 'departamento']
		labels = {
        "codigo": "Código",
        "nombre": "Nombre",
        "unidadesCredito": "Unidades de Crédito",
        "horasTeoria": "Horas de Teoria",
        "horasPractica": "Horas de Práctica",
        "horasLab": "Horas de Laboratorio",
        "requisitos": "Requisitos",
        "departamento": "Departamento"
    	}

class RegistrarProfForm(ModelForm):
	def __init__(self, user, *args, **kwargs):
		super(RegistrarProfForm, self).__init__(*args, **kwargs)
		self.user = user
		if kwargs and kwargs['instance']:
			profesor = kwargs['instance']
			self.fields['asignaturas'].queryset =\
					Asignatura.objects.all()
		if not self.user.is_anonymous:
			departamento =\
					Profesor.objects.get(user=self.user).departamento
			self.fields['departamento'].queryset =\
					Departamento.objects.filter(codigo=departamento.codigo)

	class Meta():
		model = Profesor
		fields = ['nombre', 'apellido', 'cedula',
		'disponibilidad', 'departamento', 'email', 'asignaturas']
		labels = {
        "nombre": "Nombre",
        "apellido": "Apellido",
        "cedula": "Cédula",
        "disponibilidad": "Disponibilidad",
        "departamento": "Departamento",
        "email": "e-mail",
        "asignaturas": "Asignaturas"
    	}

class ProfSeleccionaAsignaturaForm(ModelForm):
	def __init__(self, user, *args, **kwargs):
		super(ProfSeleccionaAsignaturaForm, self).__init__(*args, **kwargs)
		self.user = user
		if kwargs and kwargs['instance']:
			profesor = kwargs['instance']
			#self.fields['materia'] = django_filters.MultipleChoiceFilter(queryset=Asignatura.objects.all(),
        #widget=forms.CheckboxSelectMultiple)
			self.fields['materia'].queryset =\
					Asignatura.objects.all()
		if not self.user.is_anonymous:
			self.fields['profesor'].queryset =\
					Profesor.objects.filter(user=self.user)
			departamento =\
					Profesor.objects.get(user=self.user).departamento
			self.fields['departamento'].queryset =\
					Departamento.objects.filter(codigo=departamento.codigo)

	class Meta():
		model = Oferta
		fields = [ 'trimestre','profesor','materia','preferencia','departamento']
		labels = {
        "trimestre": "Trimestre",
        "profesor": "Profesor",
        "materia": "Materia",
        "preferencia":"Preferencia" ,
        "departamento": "Departamento"
    	}

class SignUpForm(UserCreationForm):
	departamento = forms.CharField(label='Departamento', max_length=2, validators=[RegexValidator('^[a-zA-Z]{2}$',message="Formato de código incorrecto")])
	nombre = forms.CharField(max_length=50)
	apellido = forms.CharField(max_length=50)
	cedula = forms.CharField(max_length=12)
	email = forms.CharField(max_length=200)

	class Meta:
		model = User
		fields = ('nombre', 'apellido', 'cedula', 'departamento', 'email', 'username', 'password1', 'password2')

class AuthForm(AuthenticationForm):
	class Meta:
		model = User
		fields = ('username', 'password')
