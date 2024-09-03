from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('exercicio1.urls')),
    path('', include('exercicio2.urls')),
    path('', include('exercicio3.urls')),
    ]
