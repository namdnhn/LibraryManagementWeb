from django.urls import path
from . import views

urlpatterns = [
    path('home', views.index, name='home'),
    path('', views.listbook),
    path('book/<int:id>/', views.bookpage),
]