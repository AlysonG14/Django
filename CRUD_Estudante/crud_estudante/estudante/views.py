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

@api_view(['POST'])
def criar_aluno(request):
    if request.method == 'POST':
        serializer = AlunoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)