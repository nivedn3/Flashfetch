# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-06 16:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0007_deals_activate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deals',
            name='deal_activate',
            field=models.CharField(max_length=10000),
        ),
    ]
