# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-19 09:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20190918_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='infofundo',
            name='rend_cota_mes_12',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='infofundo',
            name='rend_cota_mes_total',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
