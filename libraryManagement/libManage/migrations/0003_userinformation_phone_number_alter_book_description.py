# Generated by Django 4.1.3 on 2022-12-02 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libManage', '0002_book_publisher_userinformation_bookcopies_borrowed_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinformation',
            name='phone_number',
            field=models.CharField(default=123, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(),
        ),
    ]
