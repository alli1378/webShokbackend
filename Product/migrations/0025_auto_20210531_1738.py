# Generated by Django 3.1.7 on 2021-05-31 13:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_auto_20210427_1347'),
        ('Product', '0024_auto_20210531_1540'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productspecialrelation',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='productspecialrelation',
            name='category',
        ),
        migrations.RemoveField(
            model_name='productspecialrelation',
            name='favourite',
        ),
        migrations.RemoveField(
            model_name='productspecialrelation',
            name='product',
        ),
        migrations.RemoveField(
            model_name='productspecialrelation',
            name='seller',
        ),
        migrations.RemoveField(
            model_name='special',
            name='special',
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='Product.brand', verbose_name='برند'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(related_name='product', to='blog.Category', verbose_name='دسته بندی محصول'),
        ),
        migrations.AddField(
            model_name='product',
            name='favourite',
            field=models.ManyToManyField(blank=True, default=None, related_name='favourite_product', to=settings.AUTH_USER_MODEL, verbose_name='محصولات مورد علاقه ی شما'),
        ),
        migrations.AddField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='product_seller', to=settings.AUTH_USER_MODEL, verbose_name='فروشنده'),
        ),
        migrations.AddField(
            model_name='special',
            name='product',
            field=models.ManyToManyField(blank=True, default=None, related_name='product_shirt', to='Product.Product', verbose_name='محصولات'),
        ),
        migrations.DeleteModel(
            name='Gallery',
        ),
        migrations.DeleteModel(
            name='ProductSpecialRelation',
        ),
    ]
