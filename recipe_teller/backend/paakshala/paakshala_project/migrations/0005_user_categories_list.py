# Generated by Django 3.0.3 on 2024-04-08 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paakshala_project', '0004_auto_20240407_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='categories_list',
            field=models.TextField(default=''),
        ),
    ]
