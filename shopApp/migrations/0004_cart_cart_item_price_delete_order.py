# Generated by Django 4.2.1 on 2023-05-14 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0003_remove_order_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='cart_item_price',
            field=models.FloatField(default=0),
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]