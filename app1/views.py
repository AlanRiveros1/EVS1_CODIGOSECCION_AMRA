from django.shortcuts import render
from django.http import httpresponse

# Create your views here.

def vistaUno(request):
    html="""

<h1>"Hola Mundo app1"</h1>

"""

    return httpresponse