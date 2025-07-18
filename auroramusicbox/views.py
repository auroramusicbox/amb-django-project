from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>AMB</h1><p>hello world</p>")

# Create your views here.
