from django.shortcuts import render, redirect, get_object_or_404
from .models import Livros
from .form import LivrosForm

# Create your views here.

def lista_crud(request):
    lista_crud = Livros.objects.all()
    return render(request, 'crud/lista_crud.html', {'lista_crud' : lista_crud})

def book_create(request):
    if request.method == "POST":
        form = LivrosForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect ('lista_crud')
    else:
        form = LivrosForm()

    return render(request, 'crud/criar.html', {'form': form})

def book_views(request, pk):
    if request.method == "POST":
        book = get_object_or_404(Livros, pk=pk)

    return render(request, 'crud/detalhes_produtos.html', {'book' : book})

def book_update(request, pk):
    book = get_object_or_404(Livros, pk=pk)
    if request.method == "POST":
        form = LivrosForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
        return redirect('lista_crud')
    else:
        form = LivrosForm()
    return render(request, 'crud/criar.html', {'form': form})

def delete_book(request, pk):
    book = get_object_or_404(Livros, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('lista_crud')
    return render(request, 'crud/delete.html', {'book': book})
