# Generated by Django 3.0.3 on 2024-04-08 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paakshala_project', '0008_auto_20240408_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='user',
            field=models.CharField(default='', max_length=100),
        ),
    ]