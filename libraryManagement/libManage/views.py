from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
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
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        raise Http404("Bai viet khong ton tai")
    return render(request, 'blog/post.html', {'post': post})
