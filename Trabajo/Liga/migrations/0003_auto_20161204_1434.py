# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-04 13:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Liga', '0002_auto_20161202_1856'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipo',
            old_name='nombre',
            new_name='nombreequipo',
        ),
        migrations.RenameField(
            model_name='jornada',
            old_name='numero',
            new_name='numJornada',
        ),
    ]
