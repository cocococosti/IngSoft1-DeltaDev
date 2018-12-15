## Detalles de la Implementación (MTV – Modelo Template Vista) 
### Sprint 1 
**2.1 Agregar Asignatura al Catálogo**
* Modelo: Clases Asignatura, Departamento en models.py 
* Template:  *registroAsignatura.html* en el directorio Asignaturas > templates > Asignaturas
* Vista: Función *registroAsignaturas(request)* de views.py

**2.2 Buscar Asignaturas en el Catálogo**

Funcionalidad de búsqueda en el la tabla de asignaturas ubicado en la carpeta Asignaturas > static > js > tablaAsignatura.js. Esta es parte del plug-in data tables de JQuery.

**2.3 Modificar Asignaturas en el Catálogo**
* Modelo: El mismo modelo de la historia 2.1
* Template:  *modificarAsignatura.html*  en el directorio Asignatura > templates > Asignatura
* Vista: Función *modificarAsignatura(request, código)* de views.py en el directorio Asignaturas y función *tablaAsignaturas(request)* para editar la entrada de la tabla directamente en el botón “Modificar” 

**2.4 Eliminar Asignaturas del Catálogo**
* Modelo: El mismo modelo de la historia 2.1
* Template:  *tablaAsignaturas.html* en el directorio Asignatura> templates> Asignatura
* Vista: Funcion tablaAsignaturas(request) para eliminar la entrada de la tabla en el botón “Eliminar”
 
**2.5 Listar Asignaturas del Catálogo**

Funcionalidad del plug-in data tables de JQuery, ubicado en la carpeta Asignaturas > static > js > tablaAsignatura.js.

### Sprint 2
**Integración de épica 1 desarrollada por BIG Developers**
* Modelo: Clases Profesor, Disponibilidad en models.py
* Template: *registroProfesor.html*, *modificarProfesor.html*, *tablaProfesores.html* en Asignaturas > templates > Asignaturas
* Vista: *tablaProfesores(request)*, *registroProfesores(request)*, *modificarProfesor(request, codigo)* en views.py

**3.1 Seleccionar Asignaturas, 3.2 Seleccionar Candidatos**
* Modelo: Clase Oferta en models.py
* Template: *tablaOferta.html* en Asignaturas > templates > Asignaturas
* Vista: *tablaOferta(request)* en views.py

**3.3 Presentar Opciones** 
* Modelo: Igual que en las historias 3.1, 3.2
* Template: *tablaOferta.html* en Asignaturas > templates > Asignaturas
* Vista: *tablaOferta(request)*, *send_email(jefe, request)* en views.py

**3.4 Completar Asginación**
* Modelo: Igual que en las historias 3.1, 3.2
* Template: *tablaOferta.html*, *modificarOferta.html* en Asignaturas > templates > Asignaturas
* Vista: *tablaOferta(request)*, *modificarOferta(request, id)* en views.py

**4.1 Seleccionar Preferencias**
* Modelo: Igual que en las historias 3.1, 3.2
* Template: *dictaProfesor.html* en Asignaturas > templates > Asignaturas
* Vista: *seleccionMatProfesores(request, ci)* en views.py


