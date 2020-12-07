from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# represents the HTTP request that user made to get the data
def index(request):
    return render(request, "hello/index.html")

def brian(request):
    return HttpResponse("Hello, Brian")

def andrew(request):
    return HttpResponse("hello, me!")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize(), "date": 12
    })
