# Generated by Django 3.1.7 on 2021-07-16 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('d', 'فعال'), ('p', 'غیر فعال')], default=None, max_length=10, verbose_name='وضعیت'),
        ),
    ]
