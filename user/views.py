from django.shortcuts import render, redirect
from rest_framework.response import Response
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from .forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import json
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from .models import Dot, Cmp, Information, InformationDot
from rest_framework.decorators import api_view
from rest_framework import status
from . import serializers
import datetime
import requests


@login_required(login_url='login')
def homePage(request):
    return render(request, 'success.html')


@never_cache
def loginPage(request):
    form = UserForm()
    nxt = request.GET.get("next", '/')
    if request.method == 'POST':
        if not request.POST.get('g-recaptcha-response'):
            context = {
                'form': form,
            }
            messages.info(request, 'Le captcha est obligatoire')
            return render(request, 'Login.html', context)

        username = request.POST.get('username')
        password = request.POST.get('password')
        captcha_rs = request.POST.get('g-recaptcha-response')

        url = 'https://www.google.com/recaptcha/api/siteverify'
        data = {
            'secret': settings.RECAPTCHA_PRIVATE_KEY,
            'response': captcha_rs
        }
        response = requests.post(url, data=data)
        result = json.loads(response.text)['success']

        if result and (user := authenticate(request, username=username, password=password)) is not None:
            login(request, user)
            messages.success(request, "Connecté avec succès")
            return redirect(nxt)
        else:
            messages.warning(request, "Le nom d'utilisateur ou le mot de passe est incorrect, sinon vérifiez le "
                                      "captcha")
    context = {
        'form': form,

    }

    return render(request, 'Login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')

# Dot Data


@api_view(['GET'])
@login_required
def getDotInformations(request):
    try:
        dot = Dot.objects.get(name=request.user.dot)
    except ObjectDoesNotExist:
        return Response({'Error': 'failed to fetch data'}, status=status.HTTP_401_UNAUTHORIZED)
    month = request.query_params.get('month', datetime.date.today().month)
    year = request.query_params.get('year', datetime.date.today().year)
    data = InformationDot.objects.filter(dot=dot, date__month=month, date__year=year).order_by('date')
    srl = serializers.InformationDotSerializer(data, many=True)
    srl_user = serializers.UserSerializer(request.user, many=False)
    return Response({
        'user': srl_user.data,
        'data': srl.data
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
@login_required
def getDotInformation(request, pk):
    try:
        dot = Dot.objects.get(id=pk)
        month = request.query_params.get('month', datetime.date.today().month)
        year = request.query_params.get('year', datetime.date.today().year)
        data = InformationDot.objects.filter(dot=dot, date__month=month, date__year=year).order_by('date')
    except ValidationError:
        return Response({'Error': 'not a valid id'}, status=status.HTTP_404_NOT_FOUND)
    except ObjectDoesNotExist:
        return Response({'Error': 'failed to fetch data'}, status=status.HTTP_401_UNAUTHORIZED)
    srl = serializers.InformationDotSerializer(data, many=True)
    srl_user = serializers.UserSerializer(request.user, many=False)
    return Response({
        'user': srl_user.data,
        'data': srl.data
    }, status=status.HTTP_200_OK)

# Cmp data


@api_view(['GET'])
@login_required
def getCmpInformations(request):
    try:
        dot = Dot.objects.get(name=request.user.dot)
        cmp = Cmp.objects.filter(dot_id=dot).all()
    except ObjectDoesNotExist:
        return Response({'Error': 'failed to fetch data'}, status=status.HTTP_401_UNAUTHORIZED)
    month = request.query_params.get('month', datetime.date.today().month)
    year = request.query_params.get('year', datetime.date.today().year)
    data = Information.objects.filter(cmp__in=cmp, date__month=month, date__year=year).order_by('date')
    srl = serializers.InformationSerializer(data, many=True)
    srl_user = serializers.UserSerializer(request.user, many=False)
    return Response({
        'user': srl_user.data,
        'data': srl.data
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
@login_required
def getCmpInformation(request, pk):
    try:
        cmp = Cmp.objects.get(id=pk)
        month = request.query_params.get('month', datetime.date.today().month)
        year = request.query_params.get('year', datetime.date.today().year)
        data = Information.objects.filter(cmp=cmp, date__month=month, date__year=year).order_by('date')
    except ValidationError:
        return Response({'Error': 'not a valid id'}, status=status.HTTP_404_NOT_FOUND)
    except ObjectDoesNotExist:
        return Response({'Error': 'failed to fetch data'}, status=status.HTTP_404_NOT_FOUND)
    srl = serializers.InformationSerializer(data, many=True)
    srl_user = serializers.UserSerializer(request.user, many=False)
    return Response({
        'user': srl_user.data,
        'data': srl.data
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
@login_required
def getCmpsName(request):
    try:
        dot = Dot.objects.get(name=request.user.dot)
        cmp = Cmp.objects.filter(dot_id=dot).all()
    except ObjectDoesNotExist:
        return Response({'Error': 'failed to fetch data'}, status=status.HTTP_401_UNAUTHORIZED)
    srl = serializers.CmpSerializer(cmp, many=True)
    srl_user = serializers.UserSerializer(request.user, many=False)
    return Response({
        'user': srl_user.data,
        'data': srl.data
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
@login_required
def getCmpName(request, pk):
    try:
        dot = Dot.objects.get(id=pk)
        cmp = Cmp.objects.filter(dot=dot)
    except ValidationError:
        return Response({'Error': 'not a valid id'}, status=status.HTTP_404_NOT_FOUND)
    except ObjectDoesNotExist:
        return Response({'Error': 'failed to fetch data'}, status=status.HTTP_404_NOT_FOUND)
    srl = serializers.CmpSerializer(cmp, many=True)
    srl_user = serializers.UserSerializer(request.user, many=False)
    return Response({
        'user': srl_user.data,
        'data': srl.data
    }, status=status.HTTP_200_OK)
