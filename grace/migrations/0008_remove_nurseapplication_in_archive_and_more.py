# Generated by Django 4.2.4 on 2023-09-16 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grace', '0007_remove_nurseorder_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nurseapplication',
            name='in_archive',
        ),
        migrations.AddField(
            model_name='nurseapplication',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Активная'),
        ),
    ]
