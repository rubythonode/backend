# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 12:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='is_converted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='record',
            name='is_uploaded',
            field=models.BooleanField(default=False),
        ),
    ]
