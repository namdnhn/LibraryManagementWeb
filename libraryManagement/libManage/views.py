from django.shortcuts import redirect, render
from django.http import HttpResponse, Http404
from .models import Post, Book
from .forms import RegistrationForm
from django.http import HttpResponseRedirect 
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    return render(request, 'pages/base.html')

def list(request):
    Data = {'Posts': Post.objects.all().order_by('-date')}
    return render(request, 'blog/blog.html', Data)

def post(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        raise Http404("Bai viet khong ton tai")
    return render(request, 'blog/post.html', {'post': post})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            messages.info(request, "Thanks for registering. You are now logged in.")
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return HttpResponseRedirect("/")
    else:
        form = RegistrationForm()
    return render(request, 'pages/register.html', {'form': form})

def bookpage(request):
    try:
        book = Book.objects.get(id=id)
    except Post.DoesNotExist:
        raise Http404("Sach khong ton tai")
    return render(request, 'pages/bookshowing.html', {'book': book})
