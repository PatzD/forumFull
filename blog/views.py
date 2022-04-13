from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from .models import Post
from .forms import CreateUserForm

def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'index.html', context)

def login_page(request):
    return render(request, 'login.html')

def signup_page(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            user = form.cleaned_data.get('username')

            messages.success(request, 'Account successfully created for '+user)
            return redirect("login.html")

    context = {'form': form}
    return render(request, 'signup.html', context)