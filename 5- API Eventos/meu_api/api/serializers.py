from rest_framework import serializers
from .models import *

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class EventoSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer()
    class Meta:
        model = Evento
        fields = '__all__'