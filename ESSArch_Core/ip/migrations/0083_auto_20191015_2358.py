# Generated by Django 2.2.6 on 2019-10-15 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ip', '0082_auto_20190930_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informationpackage',
            name='package_type',
            field=models.IntegerField(choices=[(0, 'SIP'), (1, 'AIC'), (2, 'AIP'), (3, 'AIU'), (4, 'DIP')], default=0, null=True, verbose_name='package type'),
        ),
    ]
