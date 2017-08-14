# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-14 02:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('name_path', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=500, null=True)),
                ('poster', models.CharField(max_length=500, null=True)),
                ('studio', models.CharField(max_length=100, null=True)),
                ('genres', models.TextField(null=True)),
                ('year_released', models.IntegerField(null=True)),
            ],
        ),
    ]
