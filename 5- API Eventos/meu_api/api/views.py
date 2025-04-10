from django.shortcuts import render
from .models import *
from .serializers import EventoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from datetime import datetime, timedelta

# Create your views here.

@api_view(['GET'])
def lista_evento(request):
    eventos = Evento.objects.all()
    categoria = request.GET.get('categoria')
    if categoria:
        eventos = eventos.filter(categoria__nome__iexact=categoria)

    data = request.GET.get('data')
    if data:
        try:
            data_formatada = datetime.strptime(data, '%Y-%m-%d').date()
            eventos = eventos.filter(data_hora=data_formatada)
        except ValueError:
            pass

    ordering = request.GET.get('ordering')
    if ordering == 'data':
        eventos = eventos.order_by('data_evento')
    elif ordering == '-data':
        eventos = eventos.order_by('-data_evento')

    quantidade = request.GET.get('quantidade')
    if quantidade:
        try:
            quantidade = int(quantidade)
            eventos = eventos[:quantidade]
        except ValueError:
            pass

    serializer = EventoSerializer(eventos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def proximo_evento(request):
    hoje = datetime.now()
    limite = hoje + timedelta(days=7)
    eventos = Evento.objects.filter(data_evento__range=(hoje, limite)).order_by('data_evento    ')
    serializer = EventoSerializer(eventos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detalhe_evento(request, pk):
    try:
        evento = Evento.objects.get(pk=pk)
    except Evento.DoesNotExist:
        return Response("{'Erro': 'Evento não Econtrado'}", status=status.HTTP_404_NOT_FOUND)
    serializer = EventoSerializer(evento)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def criar_evento(request):
    if request.method == "POST":
        serializer = EventoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT'])
def atualizar_evento(request, pk):
    try:
        evento = Evento.objects.get(pk=pk)
    except Evento.DoesNotExist:
        return Response("{'Erro'}: 'Evento não Encontrado'", status=status.HTTP_404_NOT_FOUND)
    serializer = EventoSerializer(evento, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deletar_evento(request, pk):
    try:
        evento = Evento.objects.get(pk=pk)
    except Evento.DoesNotExist:
        return Response("{'Erro'}: 'Evento não Encontrado'", status=status.HTTP_404_NOT_FOUND)
    evento.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

