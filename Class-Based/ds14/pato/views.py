from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from .models import Pato
from .serializers import PatoSerializer, LoginSerializer, DonoDoPatoSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import serializers, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

# Create your views here.

class PatoPaginacao(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10


class PatoListCreateAPIView(ListCreateAPIView):
    queryset = Pato.objects.all() # Queryset -> 
    serializer_class = PatoSerializer
    pagination_class = PatoPaginacao


    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.query_params.get('nome')
        if nome:
            queryset = queryset.filter(nome__icontains=nome)
        return queryset
    def perform_create(self, serializer):
        if serializer.validated_data['peso'] < 0:
            raise serializers.ValidationError("O peso não pode ser negativo")
        serializer.save()

class PatoRetrieveUpdateDestroyAPIViews(RetrieveUpdateDestroyAPIView):
    queryset = Pato.objects.all()
    serializer_class = PatoSerializer
    lookup_field = 'pk'

    def put(self, request, *args, **kwargs):
        request.data.get('idade')
        if int(idade) < 20:
            
            data = request.data.copy()
            data['cor'] = 'Verde'
            request._full_data = data
        return super().put(request, *args, **kwargs)
    
class LoginView(CreateAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        usuario = serializer.validated_data['usuario']
        usuario_serializer = DonoDoPatoSerializer(usuario)

        return Response({
            'usuario': usuario_serializer.data,
            'refresh': serializer.validated_data['refresh'],
            'access': serializer.validated_data['access'],}, 
            status=status.HTTP_200_OK)
    

