# Generated by Django 3.1.7 on 2021-04-17 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0010_auto_20210417_1855'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specialfield',
            name='sizePants',
        ),
        migrations.AddField(
            model_name='specialfield',
            name='sizePants',
            field=models.ManyToManyField(blank=True, default=None, null=True, related_name='sizePants', to='Product.SizePants', verbose_name='سایز شلوار'),
        ),
        migrations.RemoveField(
            model_name='specialfield',
            name='sizeShirt',
        ),
        migrations.AddField(
            model_name='specialfield',
            name='sizeShirt',
            field=models.ManyToManyField(blank=True, default=None, null=True, related_name='sizeShirt', to='Product.SizeShirt', verbose_name='سایز پیراهن'),
        ),
        migrations.RemoveField(
            model_name='specialfield',
            name='sizeShose',
        ),
        migrations.AddField(
            model_name='specialfield',
            name='sizeShose',
            field=models.ManyToManyField(blank=True, default=None, null=True, related_name='sizeShose', to='Product.SizeShose', verbose_name='سایز کفش'),
        ),
    ]
