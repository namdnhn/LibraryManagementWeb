from django.contrib import admin
from .models import Book, Category, Publisher

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name', 'slug')

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'publisher', 'genre', 'author_name', 'description', 'price', 'inStock', 'is_available', 'img']
    list_filter = ['id', 'title', 'genre']
    search_fields = ['title', 'publisher', 'author_name']
    prepopulated_fields = {'slug': ('title',)}

class PublisherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'address', 'phone']
    search_fields = ['name']


admin.site.register(Book, BookAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Category, CategoryAdmin)