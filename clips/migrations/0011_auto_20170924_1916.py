# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-24 23:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clips', '0010_auto_20170924_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='scene',
            name='description',
            field=models.CharField(max_length=2000, null=True),
        ),
    ]
