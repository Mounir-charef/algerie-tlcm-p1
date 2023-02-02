from django.shortcuts import render, redirect, HttpResponse
from .models import User
from .forms import UserForm, FormWithCaptcha
from django.contrib.auth import authenticate, login, logout


def homePage(request):
    if request.method == 'POST':
        pass

    return HttpResponse('hello')


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        recaptcha_response = request.POST.get('g-recaptcha-response')
        print(request.POST)
        if recaptcha_response and (user := authenticate(request, username=username, password=password)) is not None:
            login(request, user)
            return redirect('home')
    form = UserForm()
    context = {
        'form': form,
        'captcha': FormWithCaptcha()
    }

    return render(request, 'Login.html', context)
