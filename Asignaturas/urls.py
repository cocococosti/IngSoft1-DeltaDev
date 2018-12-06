from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'autenticacion/$', views.autenticacion, name= 'autenticacion'),
	url(r'entrar/$', views.entrar, name='entrar'),
	url(r'registrar/$', views.registrar, name='registrar'),
	url(r'inicio/$', views.inicio, name='inicio'),
	url(r'tabla-asignaturas/$', views.tablaAsignaturas, name='asignaturas'),
	url(r'tabla-profesores/$', views.tablaProfesores, name='profesores'),
	url(r'tabla-oferta/$', views.tablaOferta, name='oferta'),
	url(r'registro-asignaturas/$', views.registroAsignaturas, name='registro'),
	url(r'modificar-asignatura/(?P<codigo>[A-Z]{2}-[0-9]{4})/$', views.modificarAsignatura, name='modificar'),
	url(r'modificar-profesor/(?P<codigo>[0-9]{6,10})/$', views.modificarProfesor, name='modificarProf'),
	url(r'registro-profesores/$', views.registroProfesores, name='registro-profesor'),
	url(r'seleccionMat-profesores/$', views.seleccionMatProfesores, name='seleccionMat-profesor'),
	url(r'salir/$', views.salir, name='salir')
]
