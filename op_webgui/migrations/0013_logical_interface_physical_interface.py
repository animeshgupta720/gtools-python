# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-03 04:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('op_webgui', '0012_auto_20180503_0432'),
    ]

    operations = [
        migrations.AddField(
            model_name='logical_interface',
            name='physical_interface',
            field=models.BooleanField(default=0),
        ),
    ]
