# Generated by Django 3.0.3 on 2024-04-08 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paakshala_project', '0005_user_categories_list'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='categories_list',
            new_name='items_list',
        ),
    ]
