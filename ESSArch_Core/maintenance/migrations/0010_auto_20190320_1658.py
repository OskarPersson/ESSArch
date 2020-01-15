# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-20 15:58
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0009_auto_20190215_0843'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appraisaljob',
            options={'get_latest_by': 'start_date', 'ordering': ('-start_date',), 'permissions': (('run_appraisaljob', 'Can run appraisal job'),)},
        ),
        migrations.AlterModelOptions(
            name='conversionjob',
            options={'get_latest_by': 'start_date', 'ordering': ('-start_date',)},
        ),
        migrations.AlterField(
            model_name='appraisaljob',
            name='status',
            field=models.CharField(choices=[('FAILURE', 'FAILURE'), ('PENDING', 'PENDING'), ('RECEIVED', 'RECEIVED'), ('RETRY', 'RETRY'), ('REVOKED', 'REVOKED'), ('STARTED', 'STARTED'), ('SUCCESS', 'SUCCESS')], default='PENDING', max_length=50),
        ),
        migrations.AlterField(
            model_name='conversionjob',
            name='status',
            field=models.CharField(choices=[('FAILURE', 'FAILURE'), ('PENDING', 'PENDING'), ('RECEIVED', 'RECEIVED'), ('RETRY', 'RETRY'), ('REVOKED', 'REVOKED'), ('STARTED', 'STARTED'), ('SUCCESS', 'SUCCESS')], default='PENDING', max_length=50),
        ),
    ]
