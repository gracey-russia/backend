# Generated by Django 4.2.4 on 2023-09-16 17:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('grace', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nurseappelation',
            name='id',
        ),
        migrations.RemoveField(
            model_name='nurseappelation',
            name='visit',
        ),
        migrations.RemoveField(
            model_name='nurseapplication',
            name='id',
        ),
        migrations.RemoveField(
            model_name='nurseorder',
            name='application',
        ),
        migrations.RemoveField(
            model_name='nurseorder',
            name='id',
        ),
        migrations.RemoveField(
            model_name='nursevisit',
            name='id',
        ),
        migrations.RemoveField(
            model_name='nursevisit',
            name='order',
        ),
        migrations.RemoveField(
            model_name='wallet',
            name='id',
        ),
        migrations.AlterField(
            model_name='nurseappelation',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='nurseapplication',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='nurseorder',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='nursevisit',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
