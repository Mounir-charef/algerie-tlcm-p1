from django.shortcuts import render, redirect,HttpResponse
from .models import Utilisateur


def homePage(request):
    return HttpResponse('hello')


def loginPage(request):
    return HttpResponse('login')
