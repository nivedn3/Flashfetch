# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-05 17:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0005_auto_20161004_2220'),
    ]

    operations = [
        migrations.CreateModel(
            name='contacts_db',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.BigIntegerField()),
                ('contact_details', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='notif',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=2000)),
                ('heading', models.CharField(max_length=1000)),
                ('image', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name='deals',
            name='image',
            field=models.CharField(max_length=1000),
        ),
    ]
