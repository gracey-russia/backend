# Generated by Django 4.2.4 on 2023-09-16 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grace', '0005_nursevisit_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='nurseappelation',
            name='visit',
            field=models.ForeignKey(default='8f22d6d5-cde3-4ca5-8b15-4993e0ba7379', on_delete=django.db.models.deletion.CASCADE, related_name='appelations', to='grace.nursevisit', verbose_name='Посещение'),
            preserve_default=False,
        ),
    ]
