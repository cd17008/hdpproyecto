# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-07-13 06:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppTrans', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='puntocontrol',
            name='responsable',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AppTrans.ResponsablePunto'),
        ),
        migrations.AlterField(
            model_name='registrollegada',
            name='cod_registro',
            field=models.CharField(default='R-00000', max_length=10),
        ),
        migrations.AlterField(
            model_name='unidadtransporte',
            name='motorista',
            field=models.OneToOneField(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='AppTrans.Motorista'),
        ),
    ]