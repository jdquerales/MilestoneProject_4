# Generated by Django 3.1.7 on 2021-04-07 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210405_1543'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='location',
            options={'verbose_name_plural': 'Locations'},
        ),
        migrations.AlterModelOptions(
            name='origin',
            options={'verbose_name_plural': 'Origins'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'Products'},
        ),
    ]
