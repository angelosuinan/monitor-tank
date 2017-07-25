# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-25 10:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0005_auto_20170724_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='oxygen_level',
            field=models.FloatField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='pH_level',
            field=models.FloatField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='temperature_level',
            field=models.FloatField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='water_level',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
