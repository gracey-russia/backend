# Generated by Django 4.2.4 on 2023-11-08 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grace', '0024_errorlogs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nurseappelation',
            name='ans',
            field=models.TextField(default='', verbose_name='Ответ администратора'),
        ),
        migrations.AlterField(
            model_name='nurseappelation',
            name='comment',
            field=models.TextField(default='', verbose_name='Причина жалобы'),
        ),
    ]
