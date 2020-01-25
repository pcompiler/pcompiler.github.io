from django.shortcuts import render
from django.http import HttpResponse

from post.models import Post

def index(request):
    posts = Post.objects.all()

    for p in posts:
        ts = p.text[:286]
        p.text = ts + "..."

    context = {
        'posts': posts
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')