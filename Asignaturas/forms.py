from django import forms
from django.core.validators import RegexValidator
from Asignaturas.models import *
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class RegistrarMatForm(forms.Form):
	nombre = forms.CharField(label='Nombre de la materia', max_length=60)
	codigo = forms.CharField(label='Código de la materia', max_length=7,
					validators=[RegexValidator('^[a-zA-Z]{2}-[0-9]{4}$',
					message="Formato de código incorrecto")])
	unidadesCredito = forms.IntegerField(label='Unidades de crédito',
					   max_value=16,min_value=1)
	area = forms.CharField(label='Área', max_length=60)
	programa = forms.CharField(label='Programa al que pertenece')
	departamento = forms.CharField(label='Departamento')
	componente = forms.CharField(label='Componente')

	def clean_codigoMateria(self):
		codigo = self.cleaned_data['codigo']
		if Asignatura.objects.filter(codigo=codigo).count() > 0:
			raise ValidationError(_('La materia ya existe'), code='mat_exist')
		return codigo

