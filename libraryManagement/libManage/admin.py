from django.contrib import admin
from .models import Post, Book, BookCopies, UserInformation, Publisher

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
    list_filter = ['date']
    search_fields = ['title']

class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'publisher', 'genre', 'author_name', 'description', 'price', 'img']
    list_filter = ['id', 'title', 'genre']
    search_fields = ['title', 'publisher', 'author_name']

class BookCopiesAdmin(admin.ModelAdmin):
    list_display = ['book', 'copynum', 'branch']
    list_filter = ['book']
    search_fields = ['book']

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['user', 'fullname', 'birth_date', 'phone_number', 'address']
    search_fields = ['user']

class PublisherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'address', 'phone']
    search_fields = ['name']

admin.site.register(Post, PostAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookCopies, BookCopiesAdmin)
admin.site.register(UserInformation, UserInfoAdmin)
admin.site.register(Publisher, PublisherAdmin)