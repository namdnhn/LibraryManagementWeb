from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class UserInformation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True, unique=True)
    fullname = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=10)
    birth_date = models.DateField()
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username



