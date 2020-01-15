# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-15 07:43
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0008_auto_20180907_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appraisaljob',
            name='rule',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='jobs', to='maintenance.AppraisalRule'),
        ),
        migrations.AlterField(
            model_name='appraisaljob',
            name='status',
            field=models.CharField(choices=[('RETRY', 'RETRY'), ('FAILURE', 'FAILURE'), ('RECEIVED', 'RECEIVED'), ('PENDING', 'PENDING'), ('STARTED', 'STARTED'), ('SUCCESS', 'SUCCESS'), ('REVOKED', 'REVOKED')], default='PENDING', max_length=50),
        ),
        migrations.AlterField(
            model_name='conversionjob',
            name='rule',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='jobs', to='maintenance.ConversionRule'),
        ),
        migrations.AlterField(
            model_name='conversionjob',
            name='status',
            field=models.CharField(choices=[('RETRY', 'RETRY'), ('FAILURE', 'FAILURE'), ('RECEIVED', 'RECEIVED'), ('PENDING', 'PENDING'), ('STARTED', 'STARTED'), ('SUCCESS', 'SUCCESS'), ('REVOKED', 'REVOKED')], default='PENDING', max_length=50),
        ),
    ]
