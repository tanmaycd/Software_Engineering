# Generated by Django 3.0.3 on 2024-04-08 14:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paakshala_project', '0009_auto_20240408_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='added_on',
            field=models.DateField(default=datetime.date(2024, 4, 8)),
        ),
    ]
