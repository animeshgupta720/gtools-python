# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-10 16:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('op_webgui', '0005_auto_20180510_0052'),
    ]

    operations = [
        migrations.AddField(
            model_name='logical_interface',
            name='inet6_dhcp_client',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='logical_interface',
            name='inet_dhcp_client',
            field=models.BooleanField(default=False),
        ),
    ]
