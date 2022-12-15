from django.shortcuts import render
from .models import Book
from django.core.paginator import Paginator
from django.http import Http404
from django.db.models import Q


# Create your views here.
def index(request):
    return render(request, 'pages/base.html')

def listbook(request):
    books = Book.objects.all().filter(is_available=True)
    page = request.GET.get('page')
    page = page or 1
    paginator = Paginator(books, 6) # phan trang (3 quyen 1 trang)
    paged_books = paginator.get_page(page)
    book_count = books.count()

    return render(request, 'booklist.html', {
        'books': paged_books,
        'book_count': book_count,
    })

def bookpage(request, id):
    book = Book.objects.get(id=id)
    return render(request, 'bookshowing.html', {'book': book})

def book_number(name):
    queryset = Book.objects
    for book in queryset:
        if(book.book == name):
            return book.inStock
    return 0

def search(request):
    if 'q' in request.GET:
        q = request.GET.get('q')
        books = Book.objects.order_by('-title').filter(Q(title__icontains=q) | Q(description__icontains=q))
        page = request.GET.get('page')
        page = page or 1
        paginator = Paginator(books, 6) # phan trang (3 quyen 1 trang)
        paged_books = paginator.get_page(page)
        book_count = books.count()
    return render(request, 'booksearch.html', {
        'books': paged_books,
        'q' : q,
        'book_count': book_count
    })