# Generated by Django 4.1.3 on 2022-12-14 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_cart', '0003_remove_cart_date_added_remove_cartitem_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='cart_id',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='quantity',
        ),
    ]
