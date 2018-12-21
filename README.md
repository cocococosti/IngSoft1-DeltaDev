
# Ingeniería de Software I - Sistema de Inscripción de Postgrado Online

El proyecto presenta las bases de lo que será la implementación del Sistema de Inscripción de Postgrado Online 
de la Universidad Simón Bolívar. Utilizando la metodología de trabajo SCRUM, el equipo desarrollador en el 
periodo de Septiembre - Diciembre 2018 tiene la misión de definir e implementar los primeros componentes del software a desplegar en un tiempo no mayor a 1 año.  

## Configuración Inicial

### Requisitos

```
Python 2.7 / 3.4 / 3.5 / 3.6
Django 1.11

```

### Paquetes pip
```
django-crispy-forms 1.7.2 -- Instalación: pip install django-crispy-forms==1.7.2 
psycopg2 2.7.5            -- Instalación: pip install psycopg2 

```

### Instalación

1. Instalar requerimientos

```
 
 pip install -r requirements.txt

```

2. Configurar migraciones

```
python manage.py makemigrations

python manage.py migrate

```

3. Cargar los datos iniciales a la base de datos.

```

python manage.py loaddata db.json


```

4. Acceder al directorio donde se encuentra en el respositorio descargado de la rama master y ejecutar el siguiente comando en la terminal:

```

python manage.py runserver

```

5. Ingresar al sistema en siguiente URL:

```

http://localhost:8000/autenticacion/

```

## Correr las Pruebas

Las pruebas realizadas en el sistema siguen los lineamientos de la TDD (Test Driven Development) para lograr un software eficaz. El sistema cuenta con formularios de registro de asignaturas con sus respectivas validaciones en los campos, las pruebas fueron desarrolladas con el objetivo de que las validaciones se realicen de forma correcta. Las pruebas estan disponibles en el archivo test.py en directorio Asignaturas.

Para correr las pruebas, ejecutar el siguiente comando en la terminal:

```

python manage.py test

```

## Lanzamiento

## Software Desarrollado en

* [Django](https://docs.djangoproject.com/en/1.11/) - Framework 

## Ayuda al Usuario

* Leer el [MANUAL DE USUARIO](https://github.com/cocococosti/IngSoft1-DeltaDev/blob/master/docs/Manual_del_Usuario.md) para detalles sobre la navegación en el sistema.

* Leer [DETALLES DE LA IMPLEMENTACIÓN](https://github.com/cocococosti/IngSoft1-DeltaDev/blob/master/docs/Detalles_de_Implementacion.md) para mayor documentación del software.

## Versión

**Novedad** Se hizo un deployment del producto para las correciones realizadas del Sprint 1 y las funcionalidades agregadas del Sprint 2 y el Sprint 3 en Heroku. En el siguiente enlace puede acceder al sistema sin necesidad de realizar las configuraciones iniciales.

```
https://sistema-asignaturas-usb.herokuapp.com/autenticacion

```

## Autores

<b>Equipo Delta Developers</b>
<br>Constanza Abarca 13-10000
<br>Moisés Gonzalez 11-10406
<br>Pedro Maldonado 13-10790
<br>Denylson Romero 13-11270
<br>Fabio Suárez 12-10578
<br>Rosana García 11-10365

## Reconocimientos

* Product Owner: Prof. José Reinoza
* SCRUM Master: Fernando Gonzalez
