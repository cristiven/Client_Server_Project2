# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-10 02:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sgc', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recolector',
            old_name='contrasena',
            new_name='ciudad',
        ),
    ]
