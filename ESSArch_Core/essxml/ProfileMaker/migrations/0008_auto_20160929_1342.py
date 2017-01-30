"""
    ESSArch is an open source archiving and digital preservation system

    ESSArch Tools for Producer (ETP)
    Copyright (C) 2005-2017 ES Solutions AB

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program. If not, see <http://www.gnu.org/licenses/>.

    Contact information:
    Web - http://www.essolutions.se
    Email - essarch@essolutions.se
"""

# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-29 13:42
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ProfileMaker', '0007_auto_20160908_1428'),
    ]

    operations = [
        migrations.CreateModel(
            name='extensionPackage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('namespace', models.CharField(max_length=255)),
                ('allElements', jsonfield.fields.JSONField(null=True)),
                ('existingElements', jsonfield.fields.JSONField(null=True)),
                ('allAttributes', jsonfield.fields.JSONField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='templatepackage',
            name='extensions',
            field=models.ManyToManyField(to='ProfileMaker.extensionPackage'),
        ),
    ]
