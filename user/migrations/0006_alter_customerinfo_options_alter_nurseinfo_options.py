# Generated by Django 4.2.4 on 2023-10-09 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_nurseinfo_age_alter_nurseinfo_description_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customerinfo',
            options={'verbose_name': 'Информация о клиенте', 'verbose_name_plural': 'Информация о клиентах'},
        ),
        migrations.AlterModelOptions(
            name='nurseinfo',
            options={'verbose_name': 'Информация о сиделке', 'verbose_name_plural': 'Информация о сиделках'},
        ),
    ]
