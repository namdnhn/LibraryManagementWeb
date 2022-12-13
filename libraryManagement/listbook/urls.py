from django.urls import path
from . import views

app_name = 'listbook'
urlpatterns = [
    path('home', views.index, name='home'),
    path('', views.listbook, name='listbook'),
    path('<int:id>/', views.bookpage, name='detailed-book')
]