from django.core.validators import RegexValidator
from Asignaturas.models import *
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class RegistrarMatForm(forms.Form):
	nombre = forms.CharField(label='Nombre de la materia', max_length=60)
	codigo = forms.CharField(label='Código de la materia', max_length=7,
					validators=[RegexValidator('^[a-zA-Z]{2}-[0-9]{4}$',
					message="Formato de código incorrecto")])
	unidadesCredito = forms.IntegerField(label='Unidades de crédito',
					   max_value=16,min_value=1)
	horasTeoria = forms.IntegerField(label='Horas de Teoría', max_value=8, min_value=0)
	horasPractica = forms.IntegerField(label='Horas de Prácticas', max_value=8, min_value=0)
	horasLab = forms.IntegerField(label='Horas de Laboratorio', max_value=8, min_value=0)
	requisitos = forms.CharField(label='Requisito', max_length=60)
	departamento = forms.CharField(max_length=3)

	def clean_codigoMateria(self):
		codigo = self.cleaned_data['codigo']
		if Asignatura.objects.filter(codigo=codigo).count() > 0:
			raise ValidationError(_('La materia ya existe'), code='mat_exist')
		return codigo


class SignUpForm(UserCreationForm):
	departamento = forms.CharField(label='Departamento', max_length=2, validators=[RegexValidator('^[a-zA-Z]{2}$',message="Formato de código incorrecto")])

	class Meta:
		model = User
		fields = ('username', 'departamento', 'password1', 'password2')

class AuthForm(AuthenticationForm):
	class Meta:
		model = User
		fields = ('username', 'password')