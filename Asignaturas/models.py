from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _


# Modelos de cada Tabla y sus atributos

class Departamento(models.Model):
    codigo = models.CharField(primary_key=True, max_length=15)
    nombre = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return self.codigo + ", " + self.nombre

class Programa(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=60, unique=True)
    descripcion = models.CharField(max_length=250)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    # Unidades de Creditos necesarios por clasificacion para Doctorado 
    nroUC_BasicasEspecializacion = models.IntegerField(default=0) 
    nroUC_AreasComplementaria = models.IntegerField(default=0) 
    nroUC_Seminarios = models.IntegerField(default=0) 
    nroUC_TrabajosDirigidos = models.IntegerField(default=0) 
    nroUC_TesisDoctoral = models.IntegerField(default=0) 
    total_UC_TesisDoctoral = models.IntegerField(default=0) # Se modifica con funciones de agregacion SUM
    # Unidades de Creditos necesarios por clasificacion para Maestrias
    nroUC_Basicas = models.IntegerField(default=0) 
    nroUC_Areas = models.IntegerField(default=0) 
    nroUC_AsigComplementarias = models.IntegerField(default=0) 
    nroUC_TrabajoDeGrado = models.IntegerField(default=0)
    total_UC_Maestria = models.IntegerField(default=0) #Se modifica con funciones de agregacion SUM
    #codigoDepartamentoPertenece = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.codigo) + ", " + self.nombre + ", "+ str(self.departamento_id) + ", " + str(self.nroUC_BasicasEspecializacion) + " ," + str(self.nroUC_AreasComplementaria) + " ," + str(self.nroUC_Seminarios) + " ," + str(self.nroUC_TrabajosDirigidos) + " ," + str(self.nroUC_TesisDoctoral) + " ," + str(self.total_UC_TesisDoctoral) + " ," + str(self.nroUC_Basicas) + " ," + str(self.nroUC_Areas) + " ," + str(self.nroUC_AsigComplementarias) + " ," + str(self.nroUC_TrabajoDeGrado) + " ," + str(self.total_UC_Maestria)

class Rol(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=60,unique=True) # Profesor (2), Estudiante (3), Jefe del departamento (1)

    def __str__(self):
        return str(self.codigo) + ", " + self.nombre

class Area(models.Model):
    nombre = models.CharField(max_length=60, primary_key=True)
    programa = models.ForeignKey(Programa, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre + ", " + str(self.programa_id)

class Componente(models.Model):
    nombre = models.CharField(max_length=60, primary_key= True)
    descripcion = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre+ ", " +self.descripcion

class Asignatura(models.Model):
    codigo = models.CharField(primary_key=True,max_length=7)
    nombre = models.CharField(max_length=60)
    unidadesCredito = models.IntegerField()
    area = models.ForeignKey(Area, on_delete=models.CASCADE) 
    departamento = models.ForeignKey(Departamento, default="",on_delete=models.CASCADE)
    componente = models.ForeignKey(Componente, default="",on_delete=models.CASCADE)
    programa = models.ForeignKey(Programa, on_delete=models.CASCADE)
    # Entre las areas segun el pdf se encuentran asignaturas basicas, inteligencia artificial
    # bases de datos entre otras
    def __str__(self):
        return self.codigo + ", " + self.nombre + ", " + str(self.unidadesCredito) + ", " + str(self.departamento_id) + ", " + str(self.area_id) + ", " + self.componente_id + ", " + str(self.programa)

class Abre(models.Model):
    departamento = models.ForeignKey(Departamento, default="",on_delete=models.CASCADE)
    materia = models.ForeignKey(Asignatura, default="",on_delete=models.CASCADE)
    trimestre = models.CharField(max_length=25)

    def __str__(self):
        return self.departamento_id+ ", " +str(self.materia_id) + ", " + self.trimestre


# class UserManager(BaseUserManager):
#     """Define a model manager for User model with no username field."""
#     use_in_migrations = True

#     def _create_user(self, email, password, **extra_fields):
#         """Create and save a User with the given email and password."""
#         if not email:
#             raise ValueError('The given email must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_user(self, email, password=None, **extra_fields):
#         """Create and save a regular User with the given email and password."""
#         extra_fields.setdefault('is_staff', False)
#         extra_fields.setdefault('is_superuser', False)
#         #extra_fields.setdefault('is_active', True)
#         return self._create_user(email, password, **extra_fields)

#     def create_superuser(self, email, password, **extra_fields):
#         """Create and save a SuperUser with the given email and password."""
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_active', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self._create_user(email, password, **extra_fields)

    

# class User(AbstractBaseUser, PermissionsMixin):
#     username = None
#     email = models.EmailField(_('dirección de correo'), unique=True)
#     is_staff = models.BooleanField(
#         _('staff status'),
#         default=False,
#         help_text=_('Designates whether the user can log into this site.'),
#     )
#     is_active = models.BooleanField(
#         _('active'),
#         default=True,
#         help_text=_(
#             'Designates whether this user should be treated as active. '
#             'Unselect this instead of deleting accounts.'
#         ),)
#     is_superuser = models.BooleanField(
#         _('superuser status'),
#         default=False,
#         help_text=_('Designates whether the user can log into this site.'),
#     )
#     #is_active = models.BooleanField(_('active'), default=True)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     objects = UserManager()

#     class Meta:
#         verbose_name = _('user')
#         verbose_name_plural = _('users')

#     def get_short_name(self):
#         '''
#         Returns the short name for the user.
#         '''
#         return self.email

#     def email_user(self, subject, message, from_email=None, **kwargs):
#         '''
#         Sends an email to this User.
#         '''
#         send_mail(subject, message, from_email, [self.email], **kwargs)
    

# class Perfil(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE)
#     cedulaIdentidad = models.IntegerField(primary_key=True)
#     primerNombre = models.CharField(max_length=15)
#     segundoNombre = models.CharField(max_length=15, default="" ,blank = True)
#     primerApellido = models.CharField(max_length=15)
#     segundoApellido = models.CharField(max_length=15)
#     rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
#     codigoDepartamento1 = models.ForeignKey(Departamento, on_delete=models.CASCADE)
#     fechaRegistro = models.DateTimeField(_('fecha de registro'), auto_now_add=True)

#     def __str__(self):
#         return str(self.cedulaIdentidad) + ", "+ self.primerNombre+", "+ self.primerApellido +", "+ self.segundoApellido +", "+ str(self.rol_id) +", "+ self.codigoDepartamento1_id