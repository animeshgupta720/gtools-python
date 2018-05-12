# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-10 00:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('op_webgui', '0003_router_local_aut_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='router',
            name='local_aut_num',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='op_webgui.aut_num'),
        ),
    ]