# Generated by Django 3.0.3 on 2024-04-11 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paakshala_project', '0012_auto_20240409_0129'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_click',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='added_on',
            field=models.DateField(default='11-04-24'),
        ),
    ]
