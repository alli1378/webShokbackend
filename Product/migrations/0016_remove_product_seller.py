# Generated by Django 3.1.7 on 2021-04-18 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0015_auto_20210418_1632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='seller',
        ),
    ]
