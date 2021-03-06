# Generated by Django 2.1.1 on 2018-09-20 19:22

import clients.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_auto_20180919_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='first_name',
            field=models.CharField(max_length=30, validators=[clients.validators.validate_name]),
        ),
        migrations.AlterField(
            model_name='client',
            name='last_name',
            field=models.CharField(max_length=30, validators=[clients.validators.validate_name]),
        ),
    ]
