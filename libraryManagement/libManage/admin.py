from django.contrib import admin
from .models import Post, Book, UserInformation, Publisher, Category

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
    list_filter = ['date']
    search_fields = ['title']

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name', 'slug')

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'publisher', 'genre', 'author_name', 'description', 'price', 'inStock', 'is_available', 'img']
    list_filter = ['id', 'title', 'genre']
    search_fields = ['title', 'publisher', 'author_name']
    prepopulated_fields = {'slug': ('title',)}

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['user', 'fullname', 'birth_date', 'phone_number', 'address']
    search_fields = ['user']

class PublisherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'address', 'phone']
    search_fields = ['name']

class BorrowedAdmin(admin.ModelAdmin):
    list_display = ['id', 'reader_usr', 'book', 'copynum', 'borrowDate', 'returnDate', 'status']
    search_fields = ['id', 'reader_usr', 'book', 'returnDate']
    list_filter = ['id', 'borrowDate', 'returnDate', 'status']

admin.site.register(Post, PostAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(UserInformation, UserInfoAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Category, CategoryAdmin)