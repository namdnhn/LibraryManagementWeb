# Generated by Django 4.1.3 on 2022-12-04 10:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('libManage', '0003_userinformation_phone_number_alter_book_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='book',
            name='url_img',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='author_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='bookcopies',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='libManage.book', unique=True),
        ),
        migrations.AlterField(
            model_name='userinformation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]
