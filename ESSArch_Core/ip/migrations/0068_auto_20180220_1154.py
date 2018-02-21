# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-20 10:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ip', '0067_auto_20180213_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='informationpackage',
            name='content_mets_create_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='informationpackage',
            name='content_mets_digest',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='informationpackage',
            name='content_mets_digest_algorithm',
            field=models.IntegerField(choices=[(0, b'MD5'), (1, b'SHA-1'), (2, b'SHA-224'), (3, b'SHA-256'), (4, b'SHA-384'), (5, b'SHA-512')], null=True),
        ),
        migrations.AddField(
            model_name='informationpackage',
            name='content_mets_path',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='informationpackage',
            name='content_mets_size',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='informationpackage',
            name='package_mets_create_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='informationpackage',
            name='package_mets_digest',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='informationpackage',
            name='package_mets_digest_algorithm',
            field=models.IntegerField(choices=[(0, b'MD5'), (1, b'SHA-1'), (2, b'SHA-224'), (3, b'SHA-256'), (4, b'SHA-384'), (5, b'SHA-512')], null=True),
        ),
        migrations.AddField(
            model_name='informationpackage',
            name='package_mets_path',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='informationpackage',
            name='package_mets_size',
            field=models.BigIntegerField(null=True),
        ),
    ]
