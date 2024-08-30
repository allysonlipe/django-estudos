# django-estudos\exercicios-avulsos\exercicio1\urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('pizzaria/<str:sabor>',views.pizzaria),
    path('idade/<int:ano>',views.idade),
    path('cor/<str:cor>',views.color),
    path('calculadora/<int:n1>/<int:n2>', views.calculadora)
]
