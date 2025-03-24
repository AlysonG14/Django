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
        book = get_object_or_404(Livros, pk=pk)
        return render(request, 'crud/book_views.html', {'book' : book})


def book_update(request, pk):
    book = get_object_or_404(Livros, pk=pk)
    if request.method == "POST":
        form = LivrosForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
        return redirect('book_views', pk=book.pk)
    else:
        form = LivrosForm(instance=book)
    return render(request, 'crud/atualizar.html', {'form': form})


def delete_book(request, pk):
    book = get_object_or_404(Livros, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('lista_crud')
    return render(request, 'crud/delete.html', {'book': book})

def search_book(request):
    # Captura os parâmetros da URL
    titulo = request.GET.get('nome', '')
    autor = request.GET.get('autor', '')
    ano = request.GET.get('ano', '')

    # Filtra os livros com base nos parâmetros, ignorando se o parâmetro está vazio
    livros = Livros.objects.all()

    if titulo:
        livros = Livros.objects.filter(titulo__icontains=titulo) # 'icontains' Começa a fazer uma busca sem o Case Sensitive
    if autor:
        livros = Livros.objects.filter(autor__icontains=autor)
    if ano:
        livros = Livros.objects.filter(ano_publicacao=ano)

    return render(request, 'crud/busca.html', {'livros' : livros})

