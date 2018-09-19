# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-09-13 13:38
from __future__ import unicode_literals

from django.db import migrations, models
import freenasUI.freeadmin.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0018_add_asigra_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asigra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asigra_bindip', freenasUI.freeadmin.models.fields.MultiSelectField(blank=True, help_text='IP addresses to bind to. If none specified, all available interfaces that are up will be listened on.', max_length=250, null=True, verbose_name='Bind IP Addresses')),
                ('asigra_path', freenasUI.freeadmin.models.fields.PathField(blank=True, max_length=255, null=True, verbose_name='Path')),
                ('asigra_postgresql_path', freenasUI.freeadmin.models.fields.PathField(blank=True, max_length=255, null=True, verbose_name='PG Path')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]