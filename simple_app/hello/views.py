from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('Страница приложения hello.')


def hello_view(request):
    name = request.GET.get('name', 'World')
    message = request.GET.get('message', 'Have a nice day')
    return HttpResponse(f'{name}, {message}')
