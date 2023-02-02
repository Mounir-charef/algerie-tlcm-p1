from django.shortcuts import render, redirect, HttpResponse
from django.conf import settings
from .forms import UserForm, FormWithCaptcha
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import urllib
import json
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def homePage(request):
    return render(request, 'success.html')


@never_cache
def loginPage(request):
    form = UserForm()
    if request.method == 'POST':
        if not request.POST.get('g-recaptcha-response'):
            context = {
                'form': form,
                'captcha': FormWithCaptcha()
            }
            messages.info(request, 'The captcha is required')
            return render(request, 'Login.html', context)

        username = request.POST.get('username')
        password = request.POST.get('password')
        captcha_rs = request.POST.get('g-recaptcha-response')

        url = 'https://www.google.com/recaptcha/api/siteverify'
        params = {
            'secret': settings.RECAPTCHA_PRIVATE_KEY,
            'response': captcha_rs
        }
        data = urllib.parse.urlencode(params).encode()
        req = urllib.request.Request(url, data=data)
        response = urllib.request.urlopen(req)
        result = json.loads(response.read().decode())['success']

        if result and (user := authenticate(request, username=username, password=password)) is not None:
            login(request, user)
            messages.success(request, "Username or Password is incorrect")
            return redirect('home')
        else:
            messages.warning(request, "Username or Password is incorrect")
    context = {
        'form': form,
        'captcha': FormWithCaptcha()
    }

    return render(request, 'Login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')
