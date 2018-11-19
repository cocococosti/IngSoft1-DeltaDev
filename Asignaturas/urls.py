from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'autenticacion/$', views.autenticacion, name= 'autenticacion'),
	url(r'entrar/$', views.entrar, name='entrar'),
	url(r'registrar/$', views.registrar, name='registrar'),
	url(r'inicio/$', views.inicio, name='inicio'),
	url(r'tabla-asignaturas/$', views.tablaAsignaturas, name='asignaturas'),
	url(r'registro-asignaturas/$', views.registroAsignaturas, name='registro'),
	url(r'salir/$', views.salir, name='salir')
]