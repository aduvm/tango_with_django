# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 03:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tango', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
