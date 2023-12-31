# Generated by Django 4.2.4 on 2023-09-03 21:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_user_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerInfo',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('region', models.CharField(choices=[('Москва', 'Москва'), ('Московская область', 'Московская область')], default='Москва', max_length=50, verbose_name='Регион')),
            ],
        ),
        migrations.CreateModel(
            name='NurseInfo',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('age', models.IntegerField(verbose_name='Возраст')),
                ('citizenship', models.CharField(max_length=50, verbose_name='Гражданство')),
                ('expirience', models.IntegerField(verbose_name='Опыт работы')),
                ('description', models.CharField(max_length=1000, verbose_name='Описание')),
            ],
        ),
    ]
