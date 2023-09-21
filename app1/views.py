from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def vistaUno(request):
    return HttpResponse("<h1>Hola Mundo app1</h1>")