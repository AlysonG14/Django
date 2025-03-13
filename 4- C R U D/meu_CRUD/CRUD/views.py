from django.shortcuts import render
from .models import Livros

# Create your views here.

def lista_crud (request):
    lista_crud = Livros.objects.all()
    return render(request, 'biblioteca_crud.html', {'lista_crud' : lista_crud})