# Generated by Django 5.0.4 on 2024-04-25 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paakshala_project', '0015_alter_item_added_on_alter_item_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='user',
            field=models.CharField(default='', max_length=200),
        ),
    ]
