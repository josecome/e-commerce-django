# Generated by Django 4.1 on 2023-08-30 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0013_cart_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='qnty',
            field=models.IntegerField(default=1),
        ),
    ]
