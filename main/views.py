# <appname>/views.py

from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def contact(request):
    return render(request, 'main/contact.html')


def platform(request):
    return render(request, 'main/contact.html')


def course(request):
    return render(request, 'main/contact.html')


def lectures(request):
    return render(request, 'main/contact.html')
