# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-28 14:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Liga', '0015_jugador_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='jugador',
            name='nombrecompleto',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
