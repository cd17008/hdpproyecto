# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-07-14 00:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppTrans', '0003_auto_20190713_0028'),
    ]

    operations = [
        migrations.AddField(
            model_name='motorista',
            name='direccion',
            field=models.CharField(max_length=40, null=True),
        ),
    ]