# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-10 19:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Liga', '0010_remove_partido_jornada'),
    ]

    operations = [
        migrations.AddField(
            model_name='partido',
            name='jornada',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Liga.Jornada'),
            preserve_default=False,
        ),
    ]
