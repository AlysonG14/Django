from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Usuario, Planeta

class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        data['usuario'] = {
            'nome': self.user.username,
            'planeta': self.user.planeta,
            'especie': self.user.especie,
        }

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class PlanetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planeta
        fields = '__all__'

