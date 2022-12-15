from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
from .models import Chat, Message
from django.contrib.auth.models import User


def index(request):
    context = {'request': request}
    return render(request, 'vamarapp/index.html', context)


def friend_page(request):
    if not request.user.is_authenticated:
        return redirect('index')
    user = User.objects.all()
    context = {'user': user}
    return render(request, 'vamarapp/friends.html', context)


def message_page(request):
    if not request.user.is_authenticated:
        return redirect('index')
    message = Message.objects.all()
    chat = Chat
    context = {"request": request, 'chat': chat, 'message': message}
    return render(request, 'vamarapp/message.html', context)


def profile_page(request):
    if not request.user.is_authenticated:
        return redirect('index')
    context = {'request': request}
    return render(request, 'vamarapp/profile.html', context)


def delete_page(request):
    if not request.user.is_authenticated:
        return redirect('index')

    u = User.objects.get(username=request.user)
    u.delete()

    return redirect('logout')


def logout_page(request):
    logout(request)
    return redirect('login')


def login_page(request):
    if request.user.is_authenticated:
        return redirect('index')
    error_message = ' '
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Неверный логин или пароль'
    context = {'request': request, "error_message": error_message}
    return render(request, "vamarapp/login.html", context)


def registration(request):
    if request.user.is_authenticated:
        return redirect('index')
    error_message = '⠀'
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            error_message = "Недопустимый пароль"
    else:
        form = RegisterForm()

    return render(request, "vamarapp/registration.html", {"form": form, 'error_message': error_message})
