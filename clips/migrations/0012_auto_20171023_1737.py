# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-23 21:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clips', '0011_auto_20170924_1916'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actor',
            old_name='name_path',
            new_name='url',
        ),
    ]
