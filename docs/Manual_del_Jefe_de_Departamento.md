# Manual del Jefe de Departamento

Este documento tiene la finalidad de ofrecer, de forma clara y sencilla, las pautas que le permitirán al usuario de la aplicación 
aprender a acceder y usar a las diversas herramientas de trabajo ofrecidas dentro del sistema. 

Se proporcina una serie de imágenes que servirán de guia para entender el comportamiento del presente módulo, es decir, los resultados
esperados al ingresar a ciertas funcionalidades específicas. 

El presente documento presentará actualizacines durante la primera etapa de desarrollo hasta la culminación del mismo.

## 1-Inicio

![Página de Ingreso](imagenes/usuarios_Inicio_login.jpg "Página de ingreso a cuenta")

### 1.1 Registro de Cuenta
  Al presionar el botón "Registrarse" verá el siguiente formulario.
![Registro de Cuenta](imagenes/usuarios_login_registrar_datos.png "Página de registro de cuenta")
  
 #### Formulario de Registro
 Para poder crear un nuev usuario de forma satisfactoria debe llenar "Todos" los campos, a continuación de ofrece una explicación con el nombre del campo y el tipo de dato se espera recibir en él.
 
 - Nombre de Usuario: dirección de correo electrónico personal/institucional.
 - Departamento: código del Departamento al cual estará adscrita la cuenta. El código se compone de dos letras Mayusculas 
 - Contraseña: codigo alfanumérico de 8 dígitos o más.
 - Confirmación: repetir nuevamente la contraseña.


### 1.1 Inicio de Sesión

Para poder acceder al sistema el usuario debe proporcionar los datos de identificación indicados en las casillas:

  - Nombre de Usuario: correo personal/institucional asociado a la cuenta.
  - Contraseña: ingresar la contraseña ingresada durante el registro de la cuenta.

  Si el ingreso fué exitoso verá la siguiente pantalla con las Herramientas de Gestión de Asignaturas:
  
  ![Menu de Asignaturas](imagenes/jefeDepartamento__pagina_principal.png "Menu de funcionalidades sobre módulo de Asignaturas")

## 2. Herramientas de Gestión de Asignaturas:
Una vez ingrese al menu de asignaturas podrá apreciar las siguientes herramientas de gestion:

  - Registrar Asignatura: muestra un Formulario con los campos requeridos para crear una nueva asignatura.
  - Ver Asignatura: lista las asignaturas existentes y ofrece las funciones CRUD.
  
### 2.1 Registrar Asignatura-Formulario (Solo para Jefes de Departamento).

  ![Menu de Asignaturas](imagenes/jefeDepartamento__Asignaturas_registrarAsignatura.png "Formulario para agregar nueva Asignatura")


### 2.2 Ver Asignaturas

![Menu de Asignaturas](imagenes/jefeDepartamento__Asignaturas_verAsignatura.png "listado de Asignaturas")

### 2.2.1 Consultar una Asignatura (Todo usuario).
(En desarrollo)
### 2.2.2 Modificar información de una asignatura (Solo para Jefes de Departamento).
(En desarrollo)
### 2.2.3 Eliminar una Asignatura (Solo para Jefes de Departamento).

1- Marcar la casilla con la Asignatura que desee eliminar.

![Menu de Asignaturas](imagenes/jefeDepartamento__Asignaturas_verAsignatura_marcarAsignatura.png "listado de Asignaturas")

2- Presione Boton Eliminar

3- Confirmación:
  Una vez presionado el botón de "Eliminar" se mostrará una ventana modal solicitado confirmar la solicitud.

  ![Menu de Asignaturas](imagenes/jefeDepartamento__Asignaturas_verAsignatura_eliminar_confirmacion.png "Modal solicitando confirmación")

Las siguientes imágenes muestran el resultado de c/u de las opciones:

  3.1- Eliminar:
 
  ![Menu de Asignaturas](imagenes/jefeDepartamento__Asignaturas_verAsignaturaActualizado.png "listado de Asignaturas") 
  
  3.1- No:

  ![Menu de Asignaturas](imagenes/jefeDepartamento__Asignaturas_verAsignatura.png "listado de Asignaturas")
