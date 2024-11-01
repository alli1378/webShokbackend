# Generated by Django 3.1.7 on 2021-04-13 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0004_auto_20210413_1123'),
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('m', 'مدیوم'), ('l', 'لارج'), ('xl', 'ایکس لارج'), ('xxl', 'دو ایکس لارج'), ('xxxl', 'سه ایکس لارج')], max_length=4, verbose_name='سایز')),
            ],
        ),
        migrations.RemoveField(
            model_name='color',
            name='sizecount',
        ),
        migrations.AddField(
            model_name='color',
            name='count',
            field=models.IntegerField(default=0, verbose_name='تعداد'),
        ),
        migrations.AlterField(
            model_name='color',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product', to='Product.product', verbose_name='محصول'),
        ),
        migrations.DeleteModel(
            name='SizeCount',
        ),
        migrations.AddField(
            model_name='color',
            name='size',
            field=models.ManyToManyField(related_name='color', to='Product.Size', verbose_name='صفات ویژه'),
        ),
    ]
