# Generated by Django 2.1.4 on 2018-12-31 09:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0009_auto_20181231_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 12, 31, 9, 49, 55, 997961, tzinfo=utc)),
        ),
    ]
