# Generated by Django 3.1.7 on 2021-07-16 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20210716_0609'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='statuss',
        ),
    ]
