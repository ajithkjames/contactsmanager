# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-17 06:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20160517_0608'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='contract',
            field=models.ForeignKey(default=b'', on_delete=django.db.models.deletion.CASCADE, to='myapp.Contract'),
        ),
    ]