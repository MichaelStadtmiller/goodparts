# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-23 03:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clips', '0005_movie_director'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='headshot',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
