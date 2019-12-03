from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def eggs(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def homepage(request):
    # View code here...
    return render(request, 'home.html', {'hithere': 'There is me'})
