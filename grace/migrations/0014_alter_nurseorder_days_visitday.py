# Generated by Django 4.2.4 on 2023-09-17 18:56

import datetime
from django.db import migrations, models
import django.db.models.deletion
import grace.choices


class Migration(migrations.Migration):

    dependencies = [
        ('grace', '0013_remove_nurseorder_in_archive_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nurseorder',
            name='days',
            field=grace.choices.ChoiceArrayField(base_field=models.CharField(blank=True, choices=[('0', 'Понедельник'), ('1', 'Вторник'), ('2', 'Среда'), ('3', 'Четверг'), ('4', 'Пятница'), ('5', 'Суббота'), ('6', 'Воскресенье')], max_length=25), blank=True, size=7, verbose_name='Дни посещения'),
        ),
        migrations.CreateModel(
            name='VisitDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('0', 'Понедельник'), ('1', 'Вторник'), ('2', 'Среда'), ('3', 'Четверг'), ('4', 'Пятница'), ('5', 'Суббота'), ('6', 'Воскресенье')], default='0', max_length=50, verbose_name='День недели')),
                ('time', models.TimeField(default=datetime.time(12, 0), verbose_name='Время посещения')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grace.nurseorder', verbose_name='Заказ')),
            ],
            options={
                'verbose_name': 'День посещения',
                'verbose_name_plural': 'Дни посещения',
            },
        ),
    ]
