# Generated by Django 4.2.7 on 2023-11-11 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_availabletime_time2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='availabletime',
            old_name='time2',
            new_name='time1',
        ),
    ]