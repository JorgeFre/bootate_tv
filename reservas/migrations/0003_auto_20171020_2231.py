# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-10-20 22:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0002_auto_20171020_2131'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tipo_Reserva',
            new_name='TipoReserva',
        ),
    ]
