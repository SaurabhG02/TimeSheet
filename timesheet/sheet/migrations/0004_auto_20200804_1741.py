# Generated by Django 2.2.12 on 2020-08-04 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheet', '0003_auto_20200804_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timesheet',
            name='attachment',
            field=models.FileField(error_messages={'required': 'The Geeks Field you enetered is not unique.'}, upload_to='media/attachment/'),
        ),
    ]