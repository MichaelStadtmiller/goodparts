# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-24 20:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clips', '0009_auto_20170924_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='studio',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='role',
            name='role',
            field=models.CharField(max_length=500, null=True),
        ),
    ]