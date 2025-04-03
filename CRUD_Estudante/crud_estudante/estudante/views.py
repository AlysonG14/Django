from django.shortcuts import render
from .models import Aluno
from .serializers import AlunoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def listar_alunos(request):
    alunos = Aluno.objects.all()
    serializer = AlunoSerializer(alunos, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def detalhe_aluno(request, pk):
    try:
        aluno = Aluno.objects.get(pk=pk)
    except Aluno.DoesNotExist:
        return Response("{'Erro': 'O aluno não foi Encontrado'}", status=status.HTTP_404_NOT_FOUND)
    serializer = AlunoSerializer(aluno)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def proximo_evento(request):
    alunos = Aluno.objects.all()


@api_view(['POST'])
def criar_aluno(request):
    if request.method == 'POST':
        serializer = AlunoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def alterar_aluno(request, pk):
    try:
        aluno = Aluno.objects.get(pk=pk)
    except Aluno.DoesNotExist:
        return Response("{'Erro': 'O aluno não foi encontrado'}", status=status.HTTP_404_NOT_FOUND)
    serializer = AlunoSerializer(aluno, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deletar_informacoes(request, pk):
    try:
        aluno = Aluno.objects.get(pk=pk)
    except Aluno.DoesNotExist:
        return Response("{'Erro': 'Informações não encontrado'}", status=status.HTTP_404_NOT_FOUND)
    aluno.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def macharete(request, text):
    import pyfiglet
    gabriel = pyfiglet.figlet_format(text)

    return Response(gabriel, status=status.HTTP_200_OK)
