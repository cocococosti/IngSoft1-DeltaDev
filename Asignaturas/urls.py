from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'inicio/$', views.inicio, name='inicio'),
	url(r'tabla-asignaturas/$', views.tablaAsignaturas, name='asignaturas'),
	url(r'registro-asignaturas/$', views.registroAsignaturas, name='registro'),
	url(r'signup/$', views.signup, name='signup'),
]