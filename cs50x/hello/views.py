from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "hello/index.html")


def vraja(request):
    return HttpResponse("Hello Vraja!")


def greet(request, name):
    return render(request, "hello/greet.html", {"name": name.capitalize()})
