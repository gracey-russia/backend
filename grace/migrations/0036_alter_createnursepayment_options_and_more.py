# Generated by Django 4.2.4 on 2024-04-04 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grace', '0035_createnursepayment_close_escrow'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='createnursepayment',
            options={'verbose_name': 'Выплата сиделке', 'verbose_name_plural': 'Выплаты сиделкам'},
        ),
        migrations.AlterField(
            model_name='createnursepayment',
            name='log',
            field=models.CharField(blank=True, max_length=5000, null=True, verbose_name='LOG'),
        ),
        migrations.CreateModel(
            name='CreateClientPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.PositiveIntegerField(verbose_name='Сумма начисления клиенту')),
                ('close_escrow', models.BooleanField(verbose_name='Закрыть ли сделку?')),
                ('log', models.CharField(blank=True, max_length=5000, null=True, verbose_name='LOG')),
                ('accumulation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grace.accumulation', verbose_name='Безопасная сделка')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grace.nurseorder', verbose_name='Заказ')),
            ],
            options={
                'verbose_name': 'Выплата клиенту',
                'verbose_name_plural': 'Выплаты клиентам',
            },
        ),
    ]