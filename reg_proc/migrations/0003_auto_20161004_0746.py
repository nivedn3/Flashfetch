# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-04 07:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reg_proc', '0002_auto_20161003_2125'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='signup',
            new_name='signup_db',
        ),
    ]
