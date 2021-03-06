# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-26 15:04
import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('essauth', '0010_auto_20180322_1449'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProxyGroup',
            fields=[
            ],
            options={
                'verbose_name': 'group',
                'proxy': True,
                'verbose_name_plural': 'groups',
                'indexes': [],
                'default_permissions': [],
            },
            bases=('auth.group',),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.CreateModel(
            name='ProxyUser',
            fields=[
            ],
            options={
                'verbose_name': 'user',
                'proxy': True,
                'verbose_name_plural': 'users',
                'indexes': [],
                'default_permissions': [],
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
