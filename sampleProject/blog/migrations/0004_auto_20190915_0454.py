# Generated by Django 2.2.5 on 2019-09-15 04:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190914_1846'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog_data',
            old_name='usename',
            new_name='username',
        ),
    ]
