# Generated by Django 2.2.12 on 2020-08-04 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timesheet',
            name='time',
            field=models.CharField(max_length=2),
        ),
    ]