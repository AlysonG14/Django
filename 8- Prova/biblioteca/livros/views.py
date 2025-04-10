from django.shortcuts import render
from .models import Livro
from .serializers import LivroSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


# Create your views here.

def lista_livros(request):
    listar_livros = Livro.objects.all().order_by('data_criacao')
    return render (request, 'URL/livros/livros.html', {'listar_livros': listar_livros})


@api_view(['GET', 'POST'])
def livros(request):
    livros = Livro.objects.all()
    serializer = LivroSerializer(livros, many=True)

    if request.method == "POST":
        serializer1 = LivroSerializer(data=request.data)
        if serializer1.is_valid():
            serializer1.save()
            return Response(serializer1.data, status=status.HTTP_201_CREATED)
        return Response(serializer1.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.data)


