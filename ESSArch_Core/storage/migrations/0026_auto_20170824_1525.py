# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-24 13:25
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0025_auto_20170801_1901'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='storageobject',
            options={'permissions': (('list_storage', 'Can list storage'), ('storage_migration', 'Storage migration'), ('storage_maintenance', 'Storage maintenance'), ('storage_management', 'Storage management'))},
        ),
    ]
