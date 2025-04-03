from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import UserAbs
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

# Create your views here.

# Cria o novo usuário

@api_view(['POST'])
def criar_usuario(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')
    telefone = request.data.get('telefone')

    # Valida os campos obrigatórios básicos

    if not username or not password or not email:
        return Response({'Erro:' 'Informações Inválidos'})
    
    # Verifica se já existe um usuário com o mesmo username, senha, email
    
    if UserAbs.objects.filter(username = username).exists():
        return Response({'Erro': 'Username já existe'})
    
    if UserAbs.objects.filter(password = password).exists():
        return Response({'Erro:' 'Senha já existe'})
    
    if UserAbs.objects.filter(email = email).exists():
        return Response({'Erro': 'Email já existe'})

# Ele vai criar um usuário administrador

    usuario = UserAbs.objects.create_superuser(
        username=username,
        password=password,
        email=email,
        telefone=telefone,
    )
    return Response({'Mensagem:' f'Usuario {username} criado com sucesso'}, status=status.HTTP_201_CREATED)

# Função de login para autenticar o usuário e geração de tokens JWT

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    # Autentica o usuário com as credenciais fornecidas: Username, Password

    usuario = authenticate(username=username, password=password)

    if usuario:

        # Gera tokens JWT (acess & refresh)
        refresh = RefreshToken.for_user(usuario)
        return Response ({
            'access': str(refresh.access_token), # acess -> 
            'refresh':str(refresh), # refresh -> 
        }, status=status.HTTP_200_OK)
    else:
        return Response({'Erro: ''Usuario ou senha inválidos'}, status=status.HTTP_401_UNAUTHORIZED)
    
# Endpoint protegido que exige autenticação JWT
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_protegida(request):
    return Response({"Mensagem": "Cadê o meu Telefone"}, status=status.HTTP_200_OK)





