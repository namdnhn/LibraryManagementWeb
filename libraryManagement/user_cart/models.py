from django.db import models
from django.contrib.auth.models import User
from listbook.models import Book
# Create your models here.

class Cart(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.user_id.username


class CartItem(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.book.title