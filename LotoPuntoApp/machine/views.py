from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Loto Punto App")

# Create your views here.
