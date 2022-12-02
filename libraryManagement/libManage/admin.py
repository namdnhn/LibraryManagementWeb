from django.contrib import admin
from .models import Post, Book, BookCopies, UserInformation

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
    list_filter = ['date']
    search_fields = ['title']

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'publisher', 'author_name', 'description']
    list_filter = ['id']
    search_fields = ['title', 'publisher', 'author_name']

class BookCopiesAdmin(admin.ModelAdmin):
    list_display = ['book', 'copynum', 'branch']
    list_filter = ['book']
    search_fields = ['book']

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['user', 'fullname', 'birth_date', 'phone_number', 'address']
    search_fields = ['user']

admin.site.register(Post, PostAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookCopies, BookCopiesAdmin)
admin.site.register(UserInformation, UserInfoAdmin)
