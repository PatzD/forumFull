from django.shortcuts import render
from requests import request
from .models import Post

def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'index.html', context)

def login_page(request):
    return render(request, 'login.html')

def signup_page(request):
    return render(request, 'signup.html')