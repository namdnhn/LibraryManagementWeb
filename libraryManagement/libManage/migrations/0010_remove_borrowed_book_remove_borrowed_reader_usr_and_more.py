# Generated by Django 4.1.3 on 2022-12-07 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_cart', '0002_alter_cartitem_book'),
        ('libManage', '0009_remove_book_url_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borrowed',
            name='book',
        ),
        migrations.RemoveField(
            model_name='borrowed',
            name='reader_usr',
        ),
        migrations.RemoveField(
            model_name='returned',
            name='book',
        ),
        migrations.RemoveField(
            model_name='returned',
            name='id',
        ),
        migrations.RemoveField(
            model_name='returned',
            name='reader_usr',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Borrowed',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Publisher',
        ),
        migrations.DeleteModel(
            name='Returned',
        ),
    ]