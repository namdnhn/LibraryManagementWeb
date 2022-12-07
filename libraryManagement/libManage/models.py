from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

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

class Borrowed(models.Model):
    reader_usr = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    copynum = models.IntegerField(default=0)
    borrowDate = models.DateTimeField(auto_now_add=True)
    returnDate = models.DateTimeField(default=borrowDate)
    STATUS = (
        ('C', 'In cart'),
        ('B', 'Borrowed')
    )
    status = models.CharField(max_length=1, choices=STATUS, default='C')

class Returned(models.Model):
    id = models.ForeignKey(Borrowed, on_delete=models.CASCADE, primary_key=True)
    reader_usr = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    copynum = models.IntegerField(default=0)
    borrowDate = models.DateTimeField()
    returnDate = models.DateTimeField()
    realReturnDate = models.DateTimeField(auto_now_add=True)


class UserInformation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True, unique=True)
    fullname = models.CharField(max_length=40)
    SEX = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others')
    )
    sex = models.CharField(max_length=1, choices=SEX, default='O')
    phone_number = models.CharField(max_length=10)
    birth_date = models.DateField()
    address = models.CharField(max_length=200)



