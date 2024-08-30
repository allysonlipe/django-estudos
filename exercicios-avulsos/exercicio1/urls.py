# django-estudos\exercicios-avulsos\exercicio1\urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Use uma string vazia '' para a rota base
    path('', views.home),
    path('primeiro',views.primeiro),
    path('segundo',views.segundo),
    path('terceiro',views.terceiro),
    path('quarto',views.quarto),
]
