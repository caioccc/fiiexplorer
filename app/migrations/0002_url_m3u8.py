# Generated by Django 2.2.16 on 2020-11-12 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='m3u8',
            field=models.TextField(blank=True, null=True),
        ),
    ]
