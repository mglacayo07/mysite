from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hola, Mundo. Estas en el index de polls")