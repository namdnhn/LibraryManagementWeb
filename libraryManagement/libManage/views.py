from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def index(request):
    # response = HttpResponse()
    # response.writelines('<h1>Hello</h1>')
    # response.write('This is library management app')
    # return response
    return render(request, 'pages/base.html')

def list(request):
    Data = {'Posts': Post.objects.all().order_by('-date')}
    return render(request, 'blog/blog.html', Data)

def post(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'blog/post.html', {'post': post})