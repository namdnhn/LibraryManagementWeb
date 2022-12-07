# Generated by Django 4.1.3 on 2022-12-05 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libManage', '0006_remove_book_url_img_borrowed_status_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, max_length=255)),
                ('category_image', models.ImageField(blank=True, upload_to='photos/categories/')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='branch',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AddField(
            model_name='book',
            name='inStock',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='book',
            name='is_available',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(default=None, max_length=100, unique=True),
        ),
        migrations.DeleteModel(
            name='BookCopies',
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libManage.category'),
        ),
    ]
