# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-08-15 03:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0031_testing_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='testing',
            name='confirmed',
            field=models.BooleanField(default=None),
        ),
    ]
