# Generated by Django 4.2.4 on 2024-03-20 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grace', '0034_createnursepayment_log'),
    ]

    operations = [
        migrations.AddField(
            model_name='createnursepayment',
            name='close_escrow',
            field=models.BooleanField(default=True, verbose_name='Закрыть ли сделку?'),
            preserve_default=False,
        ),
    ]