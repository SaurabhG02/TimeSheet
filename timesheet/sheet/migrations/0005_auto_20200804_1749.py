# Generated by Django 2.2.12 on 2020-08-04 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheet', '0004_auto_20200804_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timesheet',
            name='attachment',
            field=models.FileField(upload_to='media/attachment/'),
        ),
    ]
