# Generated by Django 4.2.4 on 2023-10-09 17:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grace', '0015_remove_nurseorder_days'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nurseapplication',
            name='care_type',
            field=models.CharField(choices=[('На несколько часов в день', 'На несколько часов в день'), ('C проживанием', 'C проживанием')], default='На несколько часов в день', max_length=300, verbose_name='На какое время нужна сиделка?'),
        ),
        migrations.AlterField(
            model_name='nurseorder',
            name='care_type',
            field=models.CharField(choices=[('На несколько часов в день', 'На несколько часов в день'), ('C проживанием', 'C проживанием')], default='На несколько часов в день', max_length=300, verbose_name='На какое время нужна сиделка?'),
        ),
        migrations.AlterField(
            model_name='nurseorder',
            name='status',
            field=models.CharField(choices=[('Ожидание оплаты', 'Ожидание оплаты'), ('Активный', 'Активный'), ('В архиве', 'В архиве')], default='Ожидание оплаты', max_length=50, verbose_name='Статус заказа'),
        ),
        migrations.AlterField(
            model_name='nursevisit',
            name='completed_date',
            field=models.DateTimeField(default=datetime.date(2000, 1, 1), verbose_name='Время выполнение'),
        ),
        migrations.AlterField(
            model_name='visitday',
            name='day',
            field=models.CharField(choices=[('-1', 'Выберите день недели'), ('0', 'Понедельник'), ('1', 'Вторник'), ('2', 'Среда'), ('3', 'Четверг'), ('4', 'Пятница'), ('5', 'Суббота'), ('6', 'Воскресенье')], default='-1', max_length=50, verbose_name='День недели'),
        ),
    ]
