from django.db import models

class Libros(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)

# Vistas.py
from django.http import HttpResponse
from models import Libro

def lista_libros(requests):
    libros = Libro.object.all()
    salida = ', '.join([l.titulo for l in libros])
    return HttpResponse(salida)

# URLS.py
from django.urls import path
from . import views

urlpatterns = [
    path('libros/', views.lista_libros, name='lista_libros'),
]