# Generated by Django 4.1.3 on 2022-12-06 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libManage', '0008_remove_book_url_img_alter_book_genre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='url_img',
        ),
    ]
