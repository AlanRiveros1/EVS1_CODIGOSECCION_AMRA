from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def vistaDos(request):
    return HttpResponse("<h1>Hola Mundo app2</h1>")

def vistaCuatro(request):
    return HttpResponse("<h1>Hola Mundo vista4</h1>")
