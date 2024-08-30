from django.shortcuts import render

# Create your views here.
def pizzaria(request, sabor):
    return render(request, 'pizzaria.html', {'sabor':sabor})

def idade(request, ano):
    idade = 2024-ano
    return render(request, 'idade.html', {'ano': ano, 'idade':idade},)

def color(request, cor):
    return render(request, 'cor-fundo.html', {'color':cor})

def calculadora(request, n1, n2):
    soma = n1 + n2
    sub = n1 - n2
    mult = n1 * n2
    divisao = n1/n2
    return render(request, 'calculadora.html', {'n1':n1, 'n2':n2, 'soma':soma, 'sub':sub, 'mult':mult, 'divisao':divisao})