# Generated by Django 3.1.7 on 2021-04-17 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]