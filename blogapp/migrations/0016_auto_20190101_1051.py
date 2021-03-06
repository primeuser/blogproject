# Generated by Django 2.1.4 on 2019-01-01 05:06

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0015_auto_20181231_1604'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='news_photo')),
                ('date_created', models.DateTimeField(blank=True, default=datetime.datetime(2019, 1, 1, 5, 6, 15, 359353, tzinfo=utc))),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.Student')),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 1, 1, 5, 6, 15, 358354, tzinfo=utc)),
        ),
    ]
