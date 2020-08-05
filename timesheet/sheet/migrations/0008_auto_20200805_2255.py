# Generated by Django 2.2.12 on 2020-08-05 17:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheet', '0007_auto_20200805_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timesheet',
            name='date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='timesheet',
            name='time',
            field=models.PositiveIntegerField(blank=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(24)]),
        ),
    ]