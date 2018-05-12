# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-11 05:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='aut_num',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asn', models.BigIntegerField(unique=True)),
                ('name', models.CharField(max_length=255)),
                ('contact', models.EmailField(blank=True, max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='neighbor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peer_ip', models.GenericIPAddressField(unpack_ipv4=True)),
                ('soft_inbound', models.BooleanField(default=True)),
                ('aut_num', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bgp.aut_num')),
            ],
        ),
    ]