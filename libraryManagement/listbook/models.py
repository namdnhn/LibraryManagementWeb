from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    category_image = models.ImageField(upload_to='photos/categories/', blank=True)

    def __str__(self):
        return self.category_name

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, default='')
    slug = models.SlugField(max_length=100, unique=True, default=None)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    genre = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
    author_name = models.CharField(max_length = 30, default='')
    description = models.TextField(default='')
    price = models.IntegerField(default=0)
    branch = models.CharField(max_length=10, default=None)
    inStock = models.IntegerField(default=0)
    is_available = models.BooleanField(default=False)
    img = models.ImageField(upload_to='images/book/', default=None, null=True)

    def __str__(self):
        return self.title

class ReviewRating(models.Model):
    product = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, blank=True)
    review = models.TextField(max_length=500, blank=True)
    rating = models.FloatField()
    ip = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject