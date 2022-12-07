from django.contrib import admin
from .models import Post, UserInformation

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
    list_filter = ['date']
    search_fields = ['title']

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['user', 'fullname', 'birth_date', 'phone_number', 'address']
    search_fields = ['user']



class BorrowedAdmin(admin.ModelAdmin):
    list_display = ['id', 'reader_usr', 'book', 'copynum', 'borrowDate', 'returnDate', 'status']
    search_fields = ['id', 'reader_usr', 'book', 'returnDate']
    list_filter = ['id', 'borrowDate', 'returnDate', 'status']

admin.site.register(Post, PostAdmin)
admin.site.register(UserInformation, UserInfoAdmin)
