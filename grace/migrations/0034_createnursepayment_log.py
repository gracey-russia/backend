# Generated by Django 4.2.4 on 2024-03-20 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grace', '0033_rename_accumulatuion_createnursepayment_accumulation'),
    ]

    operations = [
        migrations.AddField(
            model_name='createnursepayment',
            name='log',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='LOG'),
        ),
    ]