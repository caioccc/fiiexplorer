# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-22 14:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20190722_1210'),
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('published_at', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(blank=True, max_length=300, null=True)),
                ('done', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
