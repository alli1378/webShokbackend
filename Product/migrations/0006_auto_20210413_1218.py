# Generated by Django 3.1.7 on 2021-04-13 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0005_auto_20210413_1141'),
    ]

    operations = [
        migrations.CreateModel(
            name='SizePants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('m', 'مدیوم'), ('l', 'لارج'), ('xl', 'ایکس لارج'), ('xxl', 'دو ایکس لارج'), ('3xl', 'سه ایکس لارج'), ('4xl', 'چهار ایکس لارج'), ('5xl', 'پنج ایکس لارج'), ('6xl', 'شش ایکس لارج')], max_length=4, verbose_name='سایز')),
            ],
        ),
        migrations.CreateModel(
            name='SizeShirt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('m', 'مدیوم'), ('l', 'لارج'), ('xl', 'ایکس لارج'), ('xxl', 'دو ایکس لارج'), ('xxxl', 'سه ایکس لارج')], max_length=4, verbose_name='سایز')),
            ],
        ),
        migrations.CreateModel(
            name='SizeShose',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('32', '۳۲'), ('33', '۳۳'), ('34', '۳۴'), ('35', '۳۵'), ('36', '۳۶'), ('37', '۳۷'), ('38', '۳۸'), ('39', '۳۹'), ('40', '۴۰'), ('41', '۴۱'), ('42', '۴۲'), ('43', '۴۳'), ('44', '۴۴'), ('45', '۴۵'), ('46', '۴۶')], max_length=4, verbose_name='سایز')),
            ],
        ),
        migrations.CreateModel(
            name='SpecialField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(choices=[('red', 'قرمز'), ('blue', 'آبی'), ('yellow', 'زرد'), ('green', 'سبز'), ('black', 'سیاه'), ('gray', 'خاکستری'), ('white', 'سفید')], max_length=10, verbose_name='رنگ')),
                ('count', models.IntegerField(default=0, verbose_name='تعداد')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product', to='Product.product', verbose_name='محصول')),
                ('sizePants', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='color', to='Product.sizepants', verbose_name='سایز شلوار')),
                ('sizeShirt', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='color', to='Product.sizeshirt', verbose_name='سایز پیراهن')),
                ('sizeShose', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='color', to='Product.sizeshose', verbose_name='سایز کفش')),
            ],
        ),
        migrations.DeleteModel(
            name='Color',
        ),
        migrations.DeleteModel(
            name='Size',
        ),
    ]
