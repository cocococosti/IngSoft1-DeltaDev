# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-03 23:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Asignaturas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesor',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
