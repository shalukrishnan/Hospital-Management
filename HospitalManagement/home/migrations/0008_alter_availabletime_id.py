# Generated by Django 4.2.7 on 2023-11-11 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_rename_time2_availabletime_time1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availabletime',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
