# Generated by Django 2.2.5 on 2019-09-15 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190915_1530'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog_data',
            name='blog_title',
        ),
    ]
