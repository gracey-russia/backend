# Generated by Django 4.2.4 on 2023-09-03 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('customer', 'Заказчик'), ('nurse', 'Сиделка'), ('admin', 'Администратор')], default='customer', max_length=300),
        ),
    ]
