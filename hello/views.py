from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'hello/index.html')


def jose(request):
    return HttpResponse('Hello Jose')


def juan(request):
    return HttpResponse('Hello Juancito')

# rendering a template with context to allow variables in html


def greet(request, name):
    return render(request, 'hello/greet.html', {
        'name': name.capitalize()
    })
