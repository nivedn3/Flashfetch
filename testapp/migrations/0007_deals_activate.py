# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-06 16:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0006_auto_20161005_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='deals',
            name='activate',
            field=models.IntegerField(default=0),
        ),
    ]
