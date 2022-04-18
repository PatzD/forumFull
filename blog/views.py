from django.shortcuts import redirect, render
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from .models import Post
from .forms import CreateUserForm

def index(request):
    posts = Post.objects.all().order_by('-id')
    context = {
        'posts': posts,
    }

    if request.method == 'POST':
        contents = request.POST.get('post-content')
        title = request.POST.get('title')
        poster = request.user.username

        new_post = Post()

        new_post.contents = contents
        new_post.title = title
        new_post.poster = poster
        new_post.save()

        return redirect('home')

    return render(request, 'index.html', context)

def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or password incorrect')

        context = {}
        return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    return redirect('login')

def signup_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
    
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
    
                user = form.cleaned_data.get('username')
    
                messages.success(request, 'Account successfully created for '+user)
                return redirect("login")

        context = {'form': form}
        return render(request, 'signup.html', context)