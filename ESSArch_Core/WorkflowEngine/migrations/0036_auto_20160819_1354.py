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
# Generated by Django 1.9.8 on 2016-08-19 13:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WorkflowEngine', '0035_auto_20160819_1245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='step',
            name='tasks',
        ),
        migrations.RemoveField(
            model_name='steptask',
            name='step',
        ),
        migrations.RemoveField(
            model_name='steptask',
            name='task',
        ),
        migrations.DeleteModel(
            name='Step',
        ),
        migrations.DeleteModel(
            name='StepTask',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
