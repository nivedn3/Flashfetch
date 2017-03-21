# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-03 21:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg_proc', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='id',
        ),
        migrations.AddField(
            model_name='signup',
            name='otp',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='signup',
            name='referral_id',
            field=models.CharField(default='test', max_length=6, primary_key=True),
        ),
        migrations.AlterField(
            model_name='signup',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='signup',
            name='mobile',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]