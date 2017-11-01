# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-10-12 21:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proformas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proforma',
            name='tipo_proformas',
            field=models.CharField(choices=[('S', 's_individuales'), ('R', 'r_servicios'), ('P', 'p_servicios')], max_length=3),
        ),
    ]
