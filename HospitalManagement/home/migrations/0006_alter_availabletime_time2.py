# Generated by Django 4.2.7 on 2023-11-11 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_remove_availabletime_time_availabletime_time2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availabletime',
            name='time2',
            field=models.CharField(max_length=100),
        ),
    ]
