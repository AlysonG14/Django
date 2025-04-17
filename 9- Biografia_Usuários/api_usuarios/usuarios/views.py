from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView, CreateAPIView
from .models import Usuario, UsuarioAuthenticate
from .serializers import UsuarioSerializer, LoginSerializer, UsuarioSerializer, LoginSerializer2
from rest_framework.pagination import PageNumberPagination
from rest_framework import serializers, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.

class UsuarioPaginacao(PageNumberPagination):
    page_size = 7
    page_size_query_param = 'page_size'
    max_page_size = 10

class UsuarioListCreateAPIVoew(ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    pagination_class = UsuarioPaginacao
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.query_params.get('nome')
        if nome:
            queryset = queryset.filter(nome__icontains=nome)
        return queryset
    def perform_create(self, serializer):
        if serializer.validated_data['idade'] < 0:
            raise serializers.ValidationError("Não Existe idade Negativa")
        serializer.save()

class UsuarioRetrieveUpdateDestroyAPIViews(RetrieveDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    lookup_field = 'pk'

    def put(self, request, *args, **kwargs):
        idade = request.data.get('idade')
        if int(idade) < 14:

            data = request.data.copy()
            data['escolaridade'] = 'Ensino Fundamental'
            request._full_data = data
        return super().put(request, *args, **kwargs)

class LoginView(CreateAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        usuario = serializer.validated_data['usuario']
        usuario_serializer = UsuarioAuthenticate(usuario)

        return Response({
            'usuario': usuario_serializer.data,
            'refresh': serializer.validated+data['refresh'],
            'access': serializer.validated_data['access'],
        }, status=status.HTTP_200_OK)

class LoginView2(TokenObtainPairView):
    serializer_class = LoginSerializer2
    