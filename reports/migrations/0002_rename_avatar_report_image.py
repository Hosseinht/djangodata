# Generated by Django 3.2.7 on 2021-09-13 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='avatar',
            new_name='image',
        ),
    ]
