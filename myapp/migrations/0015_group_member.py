# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-18 09:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_members_contact_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='member',
            field=models.ForeignKey(default=b'', on_delete=django.db.models.deletion.CASCADE, to='myapp.Member'),
        ),
    ]