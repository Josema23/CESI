# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-28 11:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Liga', '0014_auto_20161227_2302'),
    ]

    operations = [
        migrations.AddField(
            model_name='jugador',
            name='imagen',
            field=models.ImageField(default=0, upload_to=b''),
            preserve_default=False,
        ),
    ]
