# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-22 08:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sgc', '0010_auto_20171122_0300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='municipio',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='ocupacion',
            field=models.CharField(max_length=20),
        ),
    ]
