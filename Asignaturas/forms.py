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


class SignUpForm(UserCreationForm):
	departamento = forms.CharField(label='Departamento', max_length=2, validators=[RegexValidator('^[a-zA-Z]{2}$',message="Formato de código incorrecto")])

	class Meta:
		model = User
		fields = ('username', 'departamento', 'password1', 'password2')

class AuthForm(AuthenticationForm):
	class Meta:
		model = User
		fields = ('username', 'password')