"""
    ESSArch is an open source archiving and digital preservation system

    ESSArch Core
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

import os

import django
from django.core.management.utils import get_random_secret_key

from ESSArch_Core.crypto import generate_key

default_app_config = 'ESSArch_Core.config.apps.ConfigConfig'


def initialize():
    from ESSArch_Core.config.celery import app  # noqa
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ESSArch_Core.config.settings')
    django.setup()


def load_config_template(path, version='default'):
    from pkg_resources import resource_string
    return resource_string('ESSArch_Core', 'config/{}.{}'.format(path, version)).decode('utf8')


def generate_local_settings():
    context = {
        'secret_key': get_random_secret_key(),
        'encryption_key': generate_key(),
    }

    content = load_config_template('local_settings').format(**context)
    return content
