# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-17 06:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20160517_0559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members_contact',
            name='group_code',
            field=models.ForeignKey(default=b'', on_delete=django.db.models.deletion.CASCADE, to='myapp.Group'),
        ),
    ]
