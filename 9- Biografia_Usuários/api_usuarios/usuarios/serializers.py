from rest_framework import serializers
from .models import Usuario, UsuarioAuthenticate
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        read_only_fields = ['nome']

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioAuthenticate
        fields = '__all__'

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        if username and password:
            usuario = authenticate(request=self.context.get('request'),
                                   username=username, password=password)
            
            if not usuario:
                raise serializers.ValidationError('Credencial não Autenticado', code='authorization')
            
            if not usuario.is_active:
                raise serializers.ValidationError('Conta Desativada', code='authorization')
            
            refresh = RefreshToken.for_user(usuario)

            attrs['usuario'] = usuario
            attrs['refresh'] = str(refresh)
            attrs['access'] = str(refresh.access_token)

            return attrs
        else:
            raise serializers.ValidationError('Username ou senha não inseridos', code='authorization')

class LoginSerializer2(TokenObtainPairSerializer):
    def validate(self, attrs):
        dados = super().validate(attrs)
        dados['usuario'] = {
            'nome': self.user.username,
            'bio': self.user.bio if hasattr(self.user, 'bio') else 'Bio não definida'
        }
        return dados