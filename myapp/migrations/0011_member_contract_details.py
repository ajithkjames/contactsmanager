# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-17 07:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_remove_member_contract_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='contract_details',
            field=models.ForeignKey(default=b'', on_delete=django.db.models.deletion.CASCADE, to='myapp.contract'),
        ),
    ]