from django.urls import path
from . import views

app_name = 'listbook'
urlpatterns = [
    path('', views.listbook, name='listbook'),
    path('<int:id>/', views.bookpage, name='detailed-book'),
    path('search/', views.search, name='search')
]