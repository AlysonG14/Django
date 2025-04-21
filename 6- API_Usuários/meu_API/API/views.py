from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import UsuarioSerializer
from rest_framework import status
from .models import Usuario
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

# Create your views here.

@api_view(['GET'])
def usuario(request):
    usuario = Usuario.objects.all()
    serializar = UsuarioSerializer(usuario, many=True)
    return Response(serializar.data)


@api_view(['POST'])
def create_user(request):
    nome = request.data.get('nome')
    idade = request.data.get('idade')
    telefone = request.data.get('telefone')
    endereco = request.data.get('endereco')
    escolaridade = request.data.get('escolaridade')
    animais = request.data.get('animais')

    if not idade or not telefone or not endereco:
        return Response({'Erro': 'Informações insuficiente'}, status=status.HTTP_400_BAD_REQUEST)

    if Usuario.objects.filter(nome = nome).exists():
        return Response({'Erro': 'Nome já existe'}, status=status.HTTP_400_BAD_REQUEST)
    
    if Usuario.objects.filter(telefone = telefone).exists():
        return Response({'Erro': 'Telefone já existe'}, status=status.HTTP_400_BAD_REQUEST)
    
    if Usuario.objects.filter(endereco = endereco).exists():
        return Response({'Erro': 'Endereço já existe'}, status=status.HTTP_400_BAD_REQUEST)
    
    usuario = Usuario.objects.create_user(
        username=nome, # Ele é obrigatório usar no 'Django'
        password=telefone,
        nome=nome,
        idade=idade,
        telefone=telefone,
        endereco=endereco,
        escolaridade=escolaridade,
        animais=animais
    )
    return Response({'Mensagem': f'Usuário: {nome}'}, status=status.HTTP_200_OK)

@api_view(['POST'])
def logar(request):
    nome = request.data.get('nome')
    telefone = request.data.get('telefone')

    usuario = authenticate(username=nome, password=telefone)

    if usuario:
        refresh = RefreshToken.for_user(usuario)
        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh),
            
        }, status=status.HTTP_200_OK)
    else:
        return Response({'Erro': 'Usuário ou senha incorreta'}, status=status.HTTP_401_UNAUTHORIZED)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated]) # Vamos adicionar uma permissão de segurança da rota
def usuario_logado(request):
    usuario = request.user
    serializer = UsuarioSerializer(usuario)
    return Response(serializer.data)
    

    