# Generated by Django 4.2.4 on 2023-10-19 15:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grace', '0022_remove_visitday_time_visitday_time_end_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nursevisit',
            name='time',
        ),
        migrations.AddField(
            model_name='nursevisit',
            name='time_end',
            field=models.TimeField(default=datetime.time(13, 0), verbose_name='Время конца'),
        ),
        migrations.AddField(
            model_name='nursevisit',
            name='time_start',
            field=models.TimeField(default=datetime.time(12, 0), verbose_name='Время начала'),
        ),
    ]
