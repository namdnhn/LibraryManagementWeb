from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('add_cart/<int:book_id>/<int:qtt>', views.add_cart, name='add_cart'),
]