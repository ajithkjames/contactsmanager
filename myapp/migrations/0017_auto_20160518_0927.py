# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-18 09:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_auto_20160518_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members_contact',
            name='group_code',
            field=models.IntegerField(),
        ),
    ]
