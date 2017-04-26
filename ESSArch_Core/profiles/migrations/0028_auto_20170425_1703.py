# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-25 15:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0027_auto_20170315_2129'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='submissionagreement',
            options={'ordering': ['name'], 'verbose_name': 'Submission Agreement'},
        ),
        migrations.RenameField(
            model_name='submissionagreement',
            old_name='sa_archivist_individual_additional',
            new_name='archivist_individual_additional',
        ),
        migrations.RenameField(
            model_name='submissionagreement',
            old_name='sa_archivist_individual_email',
            new_name='archivist_individual_email',
        ),
        migrations.RenameField(
            model_name='submissionagreement',
            old_name='sa_archivist_individual_name',
            new_name='archivist_individual_name',
        ),
        migrations.RenameField(
            model_name='submissionagreement',
            old_name='sa_archivist_individual_phone',
            new_name='archivist_individual_phone',
        ),
        migrations.RenameField(
            model_name='submissionagreement',
            old_name='sa_archivist_individual_role',
            new_name='archivist_individual_role',
        ),
        migrations.RenameField(
            model_name='submissionagreement',
            old_name='sa_archivist_main_additional',
            new_name='archivist_main_additional',
        ),
        migrations.RenameField(
            model_name='submissionagreement',
            old_name='sa_archivist_main_address',
            new_name='archivist_main_address',
        ),
        migrations.RenameField(
            model_name='submissionagreement',
            old_name='sa_archivist_main_email',
            new_name='archivist_main_email',
        ),
        migrations.RenameField(
            model_name='submissionagreement',
            old_name='sa_archivist_main_name',
            new_name='archivist_main_name',
        ),
        migrations.RenameField(
            model_name='submissionagreement',
            old_name='sa_archivist_main_phone',
            new_name='archivist_main_phone',
        ),
        migrations.RenameField(
            model_name='submissionagreement',
            old_name='sa_archivist_organization',
            new_name='archivist_organization',
        ),
        migrations.RenameField(
            model_name='submissionagreement',
            old_name='sa_cm_change_authority',
            new_name='cm_change_authority',
        ),
        migrations.RenameField(
            model_name='submissionagreement',
            old_name='sa_cm_change_description',
            new_name='cm_change_description',
        ),
        migrations.RenameField(
            model_name='submissionagreement',
            old_name='sa_cm_release_date',
            new_name='cm_release_date',
        ),
        migrations.RenameField(
            model_name='submissionagreement',
            old_name='sa_cm_sections_affected',
            new_name='cm_sections_affected',
        ),
        migrations.RenameField(
            model_name='submissionagreement',
            old_name='sa_cm_version',
            new_name='cm_version',
        ),
        migrations.RenameField(
            model_name='submissionagreement',
            old_name='sa_designated_community_description',
            new_name='designated_community_description',
        ),
        migrations.RenameField(
            model_name='submissionagreement',
            old_name='sa_designated_community_individual_additional',
            new_name='designated_community_individual_additional',
        ),
        migrations.RenameField(
            model_name='submissionagreement',
            old_name='sa_designated_community_individual_email',
            new_name='designated_community_individual_email',
        ),
        migrations.RenameField(
            model_name='submissionagreement',
            old_name='sa_designated_community_individual_name',
            new_name='designated_community_individual_name',
        ),
        migrations.RenameField(
            model_name='submissionagreement',
            old_name='sa_designated_community_individual_phone',
            new_name='designated_community_individual_phone',
        ),
        migrations.RenameField(
            model_name='submissionagreement',
            old_name='sa_designated_community_individual_role',
            new_name='designated_community_individual_role',
        ),
        migrations.RenameField(
            model_name='submissionagreement',
            old_name='sa_label',
            new_name='label',
        ),
        migrations.RenameField(
            model_name='submissionagreement',
            old_name='sa_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='submissionagreement',
            old_name='sa_producer_individual_additional',
            new_name='producer_individual_additional',
        ),
        migrations.RenameField(
            model_name='submissionagreement',
            old_name='sa_producer_individual_email',
            new_name='producer_individual_email',
        ),
        migrations.RenameField(
            model_name='submissionagreement',
            old_name='sa_producer_individual_name',
            new_name='producer_individual_name',
        ),
        migrations.RenameField(
            model_name='submissionagreement',
            old_name='sa_producer_individual_phone',
            new_name='producer_individual_phone',
        ),
        migrations.RenameField(
            model_name='submissionagreement',
            old_name='sa_producer_individual_role',
            new_name='producer_individual_role',
        ),
        migrations.RenameField(
            model_name='submissionagreement',
            old_name='sa_producer_main_additional',
            new_name='producer_main_additional',
        ),
        migrations.RenameField(
            model_name='submissionagreement',
            old_name='sa_producer_main_address',
            new_name='producer_main_address',
        ),
        migrations.RenameField(
            model_name='submissionagreement',
            old_name='sa_producer_main_email',
            new_name='producer_main_email',
        ),
        migrations.RenameField(
            model_name='submissionagreement',
            old_name='sa_producer_main_name',
            new_name='producer_main_name',
        ),
        migrations.RenameField(
            model_name='submissionagreement',
            old_name='sa_producer_main_phone',
            new_name='producer_main_phone',
        ),
        migrations.RenameField(
            model_name='submissionagreement',
            old_name='sa_producer_organization',
            new_name='producer_organization',
        ),
        migrations.RenameField(
            model_name='submissionagreement',
            old_name='sa_status',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='submissionagreement',
            old_name='sa_type',
            new_name='type',
        ),
    ]
