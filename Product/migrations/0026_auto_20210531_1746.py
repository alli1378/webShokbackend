# Generated by Django 3.1.7 on 2021-05-31 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0025_auto_20210531_1738'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='special',
            name='product',
        ),
        migrations.AddField(
            model_name='special',
            name='product',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='Product.product', verbose_name='محصولات'),
        ),
    ]
