# Generated by Django 4.1.3 on 2022-12-05 19:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('libManage', '0005_remove_book_url_img_book_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowed',
            name='status',
            field=models.CharField(choices=[('C', 'In cart'), ('B', 'Borrowed')], default='C', max_length=1),
        ),
        migrations.AlterField(
            model_name='borrowed',
            name='copynum',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='borrowed',
            name='returnDate',
            field=models.DateTimeField(default=models.DateTimeField(auto_now_add=True)),
        ),
        migrations.CreateModel(
            name='Returned',
            fields=[
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='libManage.borrowed')),
                ('copynum', models.IntegerField(default=0)),
                ('borrowDate', models.DateTimeField()),
                ('returnDate', models.DateTimeField()),
                ('realReturnDate', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libManage.book')),
                ('reader_usr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
