# Diseño e Implementación del Modelo ER de la Base de Datos.

 ## 1 Diseño
 ![Deseño Relacional de la Base de Datos](ER_Model.png "Modelo ER_Sprint 2")
 
   ### 1.1 Clasificación de colores:
   
```diff
  - Color azul: Entidades y relaciones previamente diseñadas e implementadas por el equipo de desarrollo Delta Developers.
  
  - Color amarillo: Entidades y relaciones previamente diseñadas por el equipo de desarrollo BIG Developers.
  
  - Color Verde: Entidades y relaciones en proceso de implementación. Durante la fase actual de desarrollo. Estos elementos del diseño pueden estar sometidos a cambios hasta su completa validación.
```  

  ### 1.2 Diccionario de Terminos empleados en el Modelo ER:

| Entidad                  | Significado                                                     |
| :----------------------: |     :------------------------------------                       |
| Asignatura               | Materia que forma parte del programa de estudios de una Carrera.|
| Departamento             | Unidad académica que se encargan del diseño, planificación, coordinación y evaluación de los programas bajo su responsabilidad, así como de llevar adelante la ejecución de esos programas|
| Profesor                 | Trabajador de la USB  que dicta las asignaturas, las asignaturas están asociadas a sus conocimientos en una determinada área|
| Oferta                   | Listado de asigaturas que un Departamento indica está en la capacidad de asegurar su impartición durante un periodo trimestral |

| Requisito                | Significado                                                     |
| :----------------------: |     :------------------------------------                       |
| es_Requisito             | Una asignatura puede o no requerir que se haya aprobado una lista espacífica de asignaturas previas.|
| esta_en                  | Una asignatura se puede ser ofertada por su Departamento en distintos períodos trimestrales.|
| dicta                    | Todo profesor tiene adociada al menos una asignatura que éste este en la capacidad de enseñar.|
| pertenece                | Cada Asignatura está asociada a un único Departamento. Un Departamento solo puede modificar y alterar las Asignaturas asociadas a él.|
| adscrito_a               | Cada Profesor está adscrito a un único Departamento.|
| pertenece_a              | Cada oferta fué creada por un único Departamento.|
