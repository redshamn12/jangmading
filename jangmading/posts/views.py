from urllib import request
from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    post = Post.objects.all()
    return render(request, 'index.html', {'post': post})

def posted(request, pk):
    post = Post.objects.get(title= pk)
    return render(request, 'post.html', {'post':post})

def page_not_found(request, exception):
    return render(request, '404.html', status=404)