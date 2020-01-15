# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-10-05 14:05
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ip', '0052_eventip_linkingagentrole'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='informationpackage',
            options={'ordering': ['id'], 'permissions': (('can_upload', 'Can upload files to IP'), ('set_uploaded', 'Can set IP as uploaded'), ('create_sip', 'Can create SIP'), ('submit_sip', 'Can submit SIP'), ('transfer_sip', 'Can transfer SIP'), ('change_sa', 'Can change SA connected to IP'), ('lock_sa', 'Can lock SA to IP'), ('unlock_profile', 'Can unlock profile connected to IP'), ('can_receive_remote_files', 'Can receive remote files'), ('receive', 'Can receive IP'), ('preserve', 'Can preserve IP'), ('preserve_dip', 'Can preserve DIP'), ('get_from_storage', 'Can get extracted IP from storage'), ('get_tar_from_storage', 'Can get packaged IP from storage'), ('get_from_storage_as_new', 'Can get IP "as new" from storage'), ('add_to_ingest_workarea', 'Can add IP to ingest workarea'), ('add_to_ingest_workarea_as_tar', 'Can add IP as tar to ingest workarea'), ('add_to_ingest_workarea_as_new', 'Can add IP as new generation to ingest workarea'), ('diff-check', 'Can diff-check IP'), ('query', 'Can query IP'), ('prepare_ip', 'Can prepare IP')), 'verbose_name': 'Information Package'},
        ),
    ]
