# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-17 08:15
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0021_auto_20170714_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ioqueue',
            name='status',
            field=models.IntegerField(blank=True, choices=[(-1, 'Inactive'), (0, 'Pending'), (2, 'Initiate'), (5, 'Progress'), (20, 'Success'), (100, 'FAIL')], default=0),
        ),
        migrations.AlterField(
            model_name='robotqueue',
            name='status',
            field=models.IntegerField(choices=[(-1, 'Inactive'), (0, 'Pending'), (2, 'Initiate'), (5, 'Progress'), (20, 'Success'), (100, 'FAIL')], default=0),
        ),
    ]
