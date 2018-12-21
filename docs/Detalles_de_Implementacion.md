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
* Vista: Funcion tablaAsignaturas(request) en views.py para eliminar la entrada de la tabla en el botón “Eliminar”
 
**2.5 Listar Asignaturas del Catálogo**

Funcionalidad del plug-in data tables de JQuery, ubicado en la carpeta Asignaturas > static > js > tablaAsignatura.js.

### Sprint 2
**Integración de épica 1 desarrollada por BIG Developers**
* Modelo: Clases Profesor, Disponibilidad en models.py
* Template: *registroProfesor.html*, *modificarProfesor.html*, *tablaProfesores.html* en Asignaturas > templates > Asignaturas
* Vista: *tablaProfesores(request)*, *registroProfesores(request)*, *modificarProfesor(request, codigo)* en views.py

**3.1 Seleccionar Asignaturas, 3.2 Seleccionar Candidatos**
* Modelo: Clase Oferta en models.py
* Template: *Ofertas.html* en Asignaturas > templates > Asignaturas para presentar la tabla de ofertas tentativas y *tablaAsignaturas.html* en el directorio Asignatura> templates> Asignatura para realizar la oferta de asignaturas mediante el boton "Ofertar Asignatura"
* Vista: *tablaOferta(request)* en views.py para el boton "Agregar Asignatura" y *tablaAsignaturas(request)* en views.py para el boton "Ofertar Asignaturas"

**3.3 Presentar Opciones** 
* Modelo: Igual que en las historias 3.1, 3.2
* Template: *Ofertas.html* en Asignaturas > templates > Asignaturas
* Vista: *tablaOferta(request)* para el boton "Enviar Oferta", *send_email(jefe, request)* para el envio de correos con el formulario especifico para cada profesor asignado en la oferta en views.py

**3.4 Completar Asginación**
* Modelo: Igual que en las historias 3.1, 3.2
* Template: *Ofertas.html*, *modificarOferta.html* en Asignaturas > templates > Asignaturas
* Vista: *tablaOferta(request)*, *modificarOferta(request, id)* en views.py para manejar botones "Modificar" y "Eliminar" en las entradas de la oferta.

**4.1 Seleccionar Preferencias**
* Modelo: Igual que en las historias 3.1, 3.2
* Template: *dictaProfesor.html* en Asignaturas > templates > Asignaturas
* Vista: *seleccionMatProfesores(request, ci)* en views.py para mostrar el formulario de selección de asignaturas a dictar para los profesores y actualizar su aceptación en la oferta.

### Sprint 3

**5.1 Crear Oferta Trimestral**

* Modelo: Clase OfertaDpto en models.py
* Template: *tablaOferta.html* en Asignaturas > templates > Asignaturas
* Vista: *tablaOfertaDpto(request)* en views.py para mostrar la oferta del departamento y *tablaOferta(request)* en views.py para guardar la oferta tentativa en la oferta del departamento mediante el botón  "Guardar Oferta Trimestral".

**5.2 Modificar Oferta de Asignatura**

* Modelo: Igual que en la historia 5.1
* Template: *tablaOferta.html* en Asignaturas > templates > Asignaturas
* Vista: *tablaOfertaDpto(request)* en views.py y *modificarOfertaDpto(request)* para manejar botón Modificar de cada entrada de la tabla de oferta departamental.

**5.3 Eliminar Oferta de Asignatura**

* Modelo: Igual que en la historia 5.1
* Template: *tablaOferta.html* en Asignaturas > templates > Asignaturas
* Vista: *tablaOfertaDpto(request)* en views.py para manejar botón Eliminar de cada entra de la tabla de oferta departamental y el botón Borrar Oferta.

**5.4 Listar Asignaturas**

* Modelo: Igual que en la historia 5.1
* Template: *tablaOferta.html* en Asignaturas > templates > Asignaturas
* Vista: *tablaOfertaDpto(request)* en views.py para presentar todas las ofertas del departamento.

**5.5 Buscar Ofertas Trimestrales**

* Modelo: Igual que en la historia 5.1
* Template: *tablaOferta.html* en Asignaturas > templates > Asignaturas
* Vista: *tablaOfertaDpto(request)* en views.py para manejar boton Cargar Oferta.

**5.6 Enviar Ofertas Trimestrales**

* Modelo: Clase OfertaDpto y Clase Coordinacion en models.py 
* Template: *tablaOferta.html* y *tablaTrimestral.html* en Asignaturas > templates > Asignaturas
* Vista: *tablaOfertaDpto(request)* en views.py para manejar boton Enviar a Coordinaciones, *send_email_coord(jefe,request)* para enviar correo a las coordinaciones y *ofertaCoord(request, id)* para presentar tabla de ofertas del departamento a la coordinación.


