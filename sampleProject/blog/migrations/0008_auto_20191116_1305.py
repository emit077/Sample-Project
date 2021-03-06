# Generated by Django 2.2.5 on 2019-11-16 13:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20191115_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 16, 13, 5, 35, 536619, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='likes',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 16, 13, 5, 35, 535849, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='requiest_list',
            name='accept_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 16, 13, 5, 35, 537650, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='requiest_list',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 16, 13, 5, 35, 537609, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user_data',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 16, 13, 5, 35, 499680, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user_data',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
