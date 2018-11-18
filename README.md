# IngSoft1-DeltaDev

Sistema de Inscripción de Postgrado Online (SIP)

Objetivo: 

Desarrollar un Repositorio del Sistema de Inscripción de Postgrado Online.

El Sistema de Inscripción de Postgrado Online es un sistema de gestión de profesores, asignaturas y trámites de inscripción trimestral para los estudiantes de postgrado. Permite gestionar la información necesaria para realizar la planificación trimestral a nivel de Departamento, consignar las disponibilidades horarias de los profesores, y permitir a los estudiantes el acceso a los trámites de manera digital, fácil, rápida y eficiente.
Funcionalidades

La primera etapa de desarrollo se encuantra actualmente a cargo de los estudiantes de la asignatura Ingeniería de Software I (CI-3715) durante el trimestre Septiembre-Diciembre 2018 en la Universidad Simón Bolívar.

# Sobre el SIP Online

Area en proceso de Desarrollo: Asignaturas.

Actualmente, el SIP Online permite:

    Gestionar las Asignaturas de postgrado por cada departamento, es decir, realizar las operaciones básicas CRUD (crear, listar, ver detalles, modificar, eliminar).

Estado Actual: En desarrollo.

Herramientas de desarrollo:

  - Lenguaje de programación Python 3.6.6 
  - Framework Django 1.11.15.
  - Gestor de Base de Datos: PostgreSql 9.9.4
  
  El resto de requerimientos se encuentran en el archivo de requerimientos (requirements.txt).

Documentación

La documentación del SIP Online se encuentra distribuida en los siguientes lugares:

    Comentarios del código, que aseguran la legibilidad del mismo siguiendo todos los estándares de calidad y convenciones de redacción de comentarios para Python y Django.
    Guía del usuario, documento de fácil lectura y acompañado de guías visuales para entender las funcionalidades del sistema, disponible aquí: guía del usuario.
    Guía del programador, documento técnico con detalles de implementación y scripts para comprender los detalles de diseño y código del sistema, disponible aquí: guía del programador.

Estos artefactos de documentación se irán actualizando progresivamente conforme se desarrolle el sistema.
Pruebas

El sistema tiene una serie de suites y casos de prueba alojados en el archivo gestion/tests.py, que se pueden ejecutar con el siguiente comando en el terminal:

python manage.py test

Las pruebas verifican integridad de modelos, métodos adicionales y algunos controladores con sus respuestas, para garantizar la calidad del código del producto.
Autores

Equipo de desarrollo de software Delta Developers.

    Constanza Abarca (13-10000)
    Pedro Maldonado(13-10790)
    Denylson Romero (13-11270)
    Fabio Suárez (12-10578)
    Moises Gonzales(11-10406)
    Rosana García (11-10365)

Contacto

Puede contactar al líder del equipo, Constanza Abarca, a través de su correo institucional 13-10000@usb.ve.
