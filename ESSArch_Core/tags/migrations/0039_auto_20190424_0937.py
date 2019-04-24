# Generated by Django 2.0.13 on 2019-04-24 07:37

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0038_auto_20190417_1051'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
            ],
            options={
                'verbose_name': 'location',
                'verbose_name_plural': 'locations',
            },
        ),
        migrations.CreateModel(
            name='LocationFunctionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='name')),
            ],
            options={
                'verbose_name': 'location function type',
                'verbose_name_plural': 'location function types',
            },
        ),
        migrations.CreateModel(
            name='LocationLevelType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='name')),
            ],
            options={
                'verbose_name': 'location level type',
                'verbose_name_plural': 'location level types',
            },
        ),
        migrations.CreateModel(
            name='MetricProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='name')),
                ('capacity', models.IntegerField(verbose_name='capacity')),
            ],
            options={
                'verbose_name': 'metric profile',
                'verbose_name_plural': 'metric profiles',
            },
        ),
        migrations.CreateModel(
            name='MetricType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='name')),
            ],
            options={
                'verbose_name': 'metric type',
                'verbose_name_plural': 'metric types',
            },
        ),
        migrations.AlterModelOptions(
            name='noderelationtype',
            options={'verbose_name': 'node relation type', 'verbose_name_plural': 'node relation types'},
        ),
        migrations.AlterModelOptions(
            name='structureunit',
            options={'permissions': (('add_structure_unit_instance', 'Can add structure unit instances'), ('change_structure_unit_instance', 'Can edit instances of structure units'), ('move_structure_unit_instance', 'Can move instances of structure units'))},
        ),
        migrations.AlterModelOptions(
            name='tagversiontype',
            options={'verbose_name': 'node type', 'verbose_name_plural': 'node types'},
        ),
        migrations.AddField(
            model_name='metricprofile',
            name='metric',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tags.MetricType', verbose_name='metric'),
        ),
        migrations.AddField(
            model_name='location',
            name='function',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tags.LocationFunctionType', verbose_name='function'),
        ),
        migrations.AddField(
            model_name='location',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tags.LocationLevelType', verbose_name='level'),
        ),
        migrations.AddField(
            model_name='location',
            name='metric',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='tags.MetricProfile', verbose_name='metric'),
        ),
        migrations.AddField(
            model_name='location',
            name='parent',
            field=mptt.fields.TreeForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='tags.Location', verbose_name='parent'),
        ),
        migrations.AddField(
            model_name='tagversion',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='tags.Location', verbose_name='location'),
        ),
        migrations.AddField(
            model_name='tagversion',
            name='metric',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='tags.MetricProfile', verbose_name='metric'),
        ),
    ]
