# Generated by Django 3.0.2 on 2020-02-01 12:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200129_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fieldparameter',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 1, 12, 29, 55, 692362, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='grid',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 1, 12, 29, 55, 691577, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 1, 12, 29, 55, 691027, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='weather',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 1, 12, 29, 55, 691985, tzinfo=utc)),
        ),
    ]
