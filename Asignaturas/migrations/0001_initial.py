# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-19 20:09
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=7, unique=True, validators=[django.core.validators.RegexValidator(message='El código de la asignatura es inválido', regex='^[A-Z]{2}-[0-9]{4}$'), django.core.validators.MaxLengthValidator(7, message='El código de la asignatura debe contener exactamente 7 caracteres'), django.core.validators.MinLengthValidator(7, message='El código de la asignatura debe contener exactamente 7 caracteres')])),
                ('nombre', models.CharField(max_length=60, validators=[django.core.validators.MaxLengthValidator(60, message='El nombre de la asignatura a lo sumo puede contener 60 caracteres'), django.core.validators.MinLengthValidator(1, message='El nombre de la asignatura debe contener al menos un caracter')])),
                ('unidadesCredito', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1, message='La asignatura debe contener al menos una unidad de crédito')])),
                ('horasTeoria', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0, message='Las horas de teoría no pueden ser negativas')])),
                ('horasPractica', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0, message='Las horas de practica no pueden ser negativas')])),
                ('horasLab', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0, message='Las horas de laboratorio no pueden ser negativas')])),
            ],
            options={
                'ordering': ['codigo'],
            },
        ),
        migrations.CreateModel(
            name='Coordinacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=200)),
                ('materias', models.ManyToManyField(blank=True, to='Asignaturas.Asignatura')),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('codigo', models.CharField(max_length=2, primary_key=True, serialize=False, validators=[django.core.validators.MaxLengthValidator(2, message='El código del Departamento debe contener exactamente 2 caracteres'), django.core.validators.MinLengthValidator(2, message='El código del Departamento debe contener exactamente 2 caracteres')])),
                ('nombre', models.CharField(max_length=60, unique=True, validators=[django.core.validators.MaxLengthValidator(60, message='El nombre del Departamento a lo sumo puede contener 60 caracteres'), django.core.validators.MinLengthValidator(1, message='El nombre de la asignatura debe ser mayor a un caracter')])),
            ],
            options={
                'ordering': ['codigo'],
            },
        ),
        migrations.CreateModel(
            name='Disponibilidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bloque', models.IntegerField(validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(1)])),
                ('dia', models.IntegerField(choices=[(1, 'Lunes'), (2, 'Martes'), (3, 'Miércoles'), (4, 'Jueves'), (5, 'Viernes'), (6, 'Sábado')], validators=[django.core.validators.MaxValueValidator(6), django.core.validators.MinValueValidator(1)])),
            ],
            options={
                'ordering': ['dia', 'bloque'],
            },
        ),
        migrations.CreateModel(
            name='OfertaCoord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trimestre', models.CharField(default='SD-18', max_length=5, validators=[django.core.validators.MaxLengthValidator(5, message='La específicación del trimestre son máximo 5 letras'), django.core.validators.MinLengthValidator(5, message='La específicación del trimestre son mínimo 5 letras')])),
                ('programa', models.CharField(default='', max_length=10)),
                ('horario', models.CharField(default='', max_length=10)),
                ('departamento', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Asignaturas.Departamento')),
                ('materia', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Asignaturas.Asignatura')),
            ],
            options={
                'ordering': ['trimestre'],
            },
        ),
        migrations.CreateModel(
            name='OfertaDpto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trimestre', models.CharField(default='SD-18', max_length=5, validators=[django.core.validators.MaxLengthValidator(5, message='La específicación del trimestre son máximo 5 letras'), django.core.validators.MinLengthValidator(5, message='La específicación del trimestre son mínimo 5 letras')])),
                ('preferencia', models.NullBooleanField(default=None)),
                ('departamento', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Asignaturas.Departamento')),
                ('materia', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Asignaturas.Asignatura')),
            ],
            options={
                'ordering': ['trimestre'],
            },
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('cedula', models.CharField(max_length=12, unique=True)),
                ('email', models.EmailField(max_length=200)),
                ('asignaturas', models.ManyToManyField(blank=True, to='Asignaturas.Asignatura')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Asignaturas.Departamento')),
                ('disponibilidad', models.ManyToManyField(blank=True, to='Asignaturas.Disponibilidad')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['cedula'],
            },
        ),
        migrations.AddField(
            model_name='ofertadpto',
            name='profesor',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='Asignaturas.Profesor'),
        ),
        migrations.AddField(
            model_name='ofertacoord',
            name='profesor',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='Asignaturas.Profesor'),
        ),
        migrations.AddField(
            model_name='departamento',
            name='jefe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='jefe_de', to='Asignaturas.Profesor'),
        ),
        migrations.AddField(
            model_name='asignatura',
            name='departamento',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Asignaturas.Departamento'),
        ),
        migrations.AddField(
            model_name='asignatura',
            name='requisitos',
            field=models.ManyToManyField(blank=True, to='Asignaturas.Asignatura'),
        ),
        migrations.AlterUniqueTogether(
            name='ofertadpto',
            unique_together=set([('trimestre', 'profesor', 'materia')]),
        ),
        migrations.AlterUniqueTogether(
            name='ofertacoord',
            unique_together=set([('trimestre', 'profesor', 'materia')]),
        ),
    ]
