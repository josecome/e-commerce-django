# Generated by Django 4.1 on 2023-08-30 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0012_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='price',
            field=models.DecimalField(decimal_places=2, default=200.0, max_digits=5),
        ),
    ]