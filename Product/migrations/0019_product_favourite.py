# Generated by Django 3.1.7 on 2021-04-21 17:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Product', '0018_auto_20210418_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='favourite',
            field=models.ManyToManyField(blank=True, default=None, related_name='favourite_product', to=settings.AUTH_USER_MODEL, verbose_name='محصولات مورد علاقه'),
        ),
    ]
