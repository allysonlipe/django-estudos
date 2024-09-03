from django.shortcuts import render

# Create your views here.
def noticia(request):
    return render(request,'noticia.html')

def login(request):
    return render(request,'login.html')

def arearestrita(request, status):
    return render(request, 'arearestrita.html', {'status':status})

def tema(request, tema):
    return render(request, 'tema.html', {'tema':tema})

def galeria(request, num):
    image_path = f'images/{num}.png'
    context = {'num':num, 'image_path':image_path}
    return render(request,'galeria.html', context)