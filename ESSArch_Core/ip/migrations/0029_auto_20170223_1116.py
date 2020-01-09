# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-23 10:16
from django.db import migrations, models
import django.db.models.deletion
from django.db.models import F
import uuid


def before_all(apps, schema_editor):
    InformationPackage = apps.get_model("ip", "InformationPackage")
    db_alias = schema_editor.connection.alias

    InformationPackage.objects.using(db_alias).filter(
        ObjectIdentifierValue__isnull=True
    ).update(ObjectIdentifierValue=F('id'))


def after_package_type(apps, schema_editor):
    InformationPackage = apps.get_model("ip", "InformationPackage")
    db_alias = schema_editor.connection.alias

    InformationPackage.objects.using(db_alias).all().update(
        package_type=0
    )


def reverse(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0006_archivepolicy'),
        ('ip', '0031_auto_20170524_1222'),
    ]

    operations = [
        migrations.RunPython(before_all, reverse),
        migrations.CreateModel(
            name='InformationPackageMetadata',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.IntegerField(null=True)),
                ('server', models.IntegerField(null=True)),
                ('server_url', models.CharField(blank=True, max_length=255)),
                ('local_path', models.CharField(blank=True, max_length=255)),
                ('blob', models.TextField(blank=True)),
                ('message_digest_algorithm', models.IntegerField(choices=[('MD5', 'MD5'), ('SHA-1', 'SHA-1'), ('SHA-224', 'SHA-224'), ('SHA-256', 'SHA-256'), ('SHA-384', 'SHA-384'), ('SHA-512', 'SHA-512')], null=True)),
                ('message_digest', models.CharField(blank=True, max_length=128)),
                ('last_changed_local', models.DateTimeField(null=True)),
                ('last_changed_external', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InformationPackageRel',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='informationpackage',
            name='OAIStype',
        ),
        migrations.AddField(
            model_name='informationpackage',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='informationpackage',
            name='create_agent_identifier_value',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='informationpackage',
            name='delivery_type',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='informationpackage',
            name='entry_agent_identifier_value',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='informationpackage',
            name='entry_date',
            field=models.DateTimeField(null=True, verbose_name='entry date'),
        ),
        migrations.AddField(
            model_name='informationpackage',
            name='generation',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='informationpackage',
            name='information_class',
            field=models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4')], null=True),
        ),
        migrations.AddField(
            model_name='informationpackage',
            name='last_changed_external',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='informationpackage',
            name='last_changed_local',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='informationpackage',
            name='linking_agent_identifier_value',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='informationpackage',
            name='message_digest',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='informationpackage',
            name='message_digest_algorithm',
            field=models.IntegerField(choices=[('MD5', 'MD5'), ('SHA-1', 'SHA-1'), ('SHA-224', 'SHA-224'), ('SHA-256', 'SHA-256'), ('SHA-384', 'SHA-384'), ('SHA-512', 'SHA-512')], null=True),
        ),
        migrations.AddField(
            model_name='informationpackage',
            name='package_type',
            field=models.IntegerField(choices=[(0, 'SIP'), (1, 'AIC'), (2, 'AIP'), (3, 'AIU'), (4, 'DIP')], null=True, verbose_name='package type'),
        ),
        migrations.RunPython(after_package_type, reverse),
        migrations.AddField(
            model_name='informationpackage',
            name='policy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='configuration.ArchivePolicy'),
        ),
        migrations.AddField(
            model_name='informationpackage',
            name='preservation_level_value',
            field=models.IntegerField(choices=[(1, 'full')], default=1),
        ),
        migrations.AlterField(
            model_name='informationpackage',
            name='Label',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='informationpackage',
            name='ObjectIdentifierValue',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='informationpackage',
            name='ObjectPath',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='informationpackagerel',
            name='aic_uuid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relaic_set', to='ip.InformationPackage'),
        ),
        migrations.AddField(
            model_name='informationpackagerel',
            name='uuid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reluuid_set', to='ip.InformationPackage'),
        ),
        migrations.AddField(
            model_name='informationpackagemetadata',
            name='ip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ip.InformationPackage'),
        ),
        migrations.AddField(
            model_name='informationpackage',
            name='information_packages',
            field=models.ManyToManyField(related_name='aic_set', through='ip.InformationPackageRel', to='ip.InformationPackage'),
        ),
        migrations.AlterUniqueTogether(
            name='informationpackagerel',
            unique_together=set([('aic_uuid', 'uuid')]),
        ),
    ]
