# Generated by Django 2.2.5 on 2019-11-12 08:08

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 12, 8, 8, 46, 676403, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='likes',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 12, 8, 8, 46, 675631, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='requiest_list',
            name='accept_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 12, 8, 8, 46, 677446, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='requiest_list',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 12, 8, 8, 46, 677407, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='requiest_list',
            name='requested_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator', to='blog.User'),
        ),
        migrations.AlterField(
            model_name='requiest_list',
            name='requested_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignee', to='blog.User'),
        ),
        migrations.AlterField(
            model_name='user',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 12, 8, 8, 46, 638453, tzinfo=utc)),
        ),
    ]