# Generated by Django 3.1.7 on 2021-07-16 11:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Product', '0027_auto_20210716_0249'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='employe',
            field=models.ManyToManyField(default=None, related_name='brand', to=settings.AUTH_USER_MODEL, verbose_name='کارمند'),
        ),
    ]
