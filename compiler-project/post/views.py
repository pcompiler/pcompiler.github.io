from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Post

def index(request):
    posts = Post.objects.all()

    for p in posts:
        ts = p.text[:286]
        p.text = ts + "..."

    context = {
        'posts': posts
    }
    return render(request, 'posts/posts.html', context)

def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    context = {
        'p': post
    }
    return render(request, 'posts/post.html', context)