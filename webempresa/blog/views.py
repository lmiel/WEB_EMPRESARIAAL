from django.shortcuts import render
from .models import Post, Category

def blog(request):
    posts = Post.objects.all().order_by('-published')
    
    for post in posts:
        print(post)
    return render(request, "blog/blog.html", {'posts':posts})