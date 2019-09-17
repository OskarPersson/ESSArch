# Generated by Django 2.2.5 on 2019-09-12 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0059_structure_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='capacity',
            field=models.IntegerField(null=True, verbose_name='capacity'),
        ),
        migrations.AddField(
            model_name='tagversion',
            name='capacity',
            field=models.IntegerField(null=True, verbose_name='capacity'),
        ),
        migrations.AlterField(
            model_name='location',
            name='metric',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='tags.MetricType', verbose_name='metric'),
        ),
        migrations.AlterField(
            model_name='tagversion',
            name='metric',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='tags.MetricType', verbose_name='metric'),
        ),
        migrations.DeleteModel(
            name='MetricProfile',
        ),
    ]