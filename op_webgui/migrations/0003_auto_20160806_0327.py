# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-06 03:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('op_webgui', '0002_auto_20160806_0310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aut_num',
            name='asn',
            field=models.BigIntegerField(unique=True),
        ),
    ]
