from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('Hello World')

def primeiro(request):
    return render(request, 'primeiro.html')

def segundo(request):
    return render(request, 'segundo.html')

def terceiro(request):
    return render(request, 'terceiro.html')

def quarto(request):
    return render(request, 'quarto.html')
