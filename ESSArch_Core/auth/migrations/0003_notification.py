# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-14 13:17
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('essauth', '0002_auto_20170622_1000'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(choices=[(10, 'debug'), (20, 'info'), (30, 'warning'), (40, 'error'), (50, 'critical')])),
                ('message', models.CharField(max_length=255)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-time_created'],
                'get_latest_by': 'time_created',
                'db_table': 'essauth_notification',
            },
        ),
    ]
