# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-06 18:07
from datetime import timedelta

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('storage', '0005_auto_20170322_1217'),
    ]

    operations = [
        migrations.CreateModel(
            name='Robot',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('device', models.CharField(max_length=255, unique=True)),
                ('online', models.BooleanField(default=False)),
                ('label', models.CharField(blank=True, max_length=255, verbose_name='Describing label for the robot')),
            ],
        ),
        migrations.CreateModel(
            name='RobotQueue',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('posted', models.DateTimeField(auto_now_add=True)),
                ('req_type', models.IntegerField(choices=[(10, 'mount'), (20, 'unmount'), (30, 'unmount (force)')])),
                ('status', models.IntegerField(choices=[(0, 'Pending'), (2, 'Initiate'), (5, 'Progress'), (20, 'Success'), (100, 'FAIL')], default=0)),
                ('robot', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='robot_queue', to='storage.Robot')),
                ('storage_medium', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='storage.StorageMedium')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='robot_queue_entries', to=settings.AUTH_USER_MODEL)),
                ('io_queue_entry', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='storage.IOQueue')),
            ],
            options={
                'get_latest_by': 'posted',
            },
        ),
        migrations.CreateModel(
            name='TapeDrive',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('device', models.CharField(max_length=255, unique=True)),
                ('idle_time', models.DurationField(default=timedelta(hours=1))),
                ('num_of_mounts', models.IntegerField(default=0)),
                ('io_queue_entry', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tape_drive', to='storage.IOQueue')),
                ('robot', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tape_drives', to='storage.Robot')),
                ('last_change', models.DateTimeField(auto_now_add=True)),
                ('drive_id', models.IntegerField()),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (20, 'Write'), (100, 'FAIL')], default=20)),
                ('locked', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TapeSlot',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('slot_id', models.IntegerField()),
                ('medium_id', models.CharField(max_length=255, unique=True, verbose_name='The id for the medium, e.g. barcode')),
                ('robot', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tape_slots', to='storage.Robot')),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (20, 'Write'), (100, 'FAIL')], default=20)),
            ],
        ),
        migrations.AlterModelOptions(
            name='tapeslot',
            options={'ordering': ('slot_id',)},
        ),
        migrations.AlterUniqueTogether(
            name='tapeslot',
            unique_together=set([('slot_id', 'robot')]),
        ),
        migrations.AddField(
            model_name='robotqueue',
            name='tape_drive',
            field=models.ForeignKey(db_constraint=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='storage.TapeDrive'),
        ),
    ]
