# Generated by Django 4.2.7 on 2023-11-11 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_availabletime_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='time1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_slot', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='booking',
            name='booked_slot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.time1'),
        ),
        migrations.DeleteModel(
            name='AvailableTime',
        ),
    ]
