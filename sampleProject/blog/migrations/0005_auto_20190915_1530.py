# Generated by Django 2.2.5 on 2019-09-15 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190915_0454'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog_data',
            old_name='AcessTo',
            new_name='notsharedwith',
        ),
        migrations.RenameField(
            model_name='blog_data',
            old_name='notAcessto',
            new_name='sharedwith',
        ),
    ]
