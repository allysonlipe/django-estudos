# django-estudos\exercicios-avulsos\exercicio1\urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('noticia/',views.noticia),
    path('login/',views.login),
    path('arearestrita/<str:status>',views.arearestrita),
    path('tema/<str:tema>',views.tema),
    path('galeria/<str:num>',views.galeria),
]
