# Generated by Django 4.2.4 on 2024-02-12 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grace', '0027_accumulation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nurseorder',
            name='care_type',
            field=models.CharField(choices=[('На несколько часов в день', 'На несколько часов в день'), ('C проживанием', 'C проживанием')], default='На несколько часов в день', max_length=300, verbose_name='Тип'),
        ),
        migrations.AlterField(
            model_name='nurseorder',
            name='cost',
            field=models.PositiveIntegerField(verbose_name='Стоимость за посещение (за неделю)'),
        ),
    ]
