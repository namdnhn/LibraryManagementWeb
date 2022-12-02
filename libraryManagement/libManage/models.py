from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    author_name = models.CharField(max_length = 30)
    description = models.TextField()

    def __str__(self):
        return self.title

class BookCopies(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, primary_key=True)
    copynum = models.IntegerField()
    branch = models.CharField(max_length=10)

class Borrowed(models.Model):
    reader_usr = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    copynum = models.IntegerField()
    returnDate = models.DateTimeField()
    borrowDate = models.DateTimeField(auto_now_add=True)

class UserInformation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)
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

