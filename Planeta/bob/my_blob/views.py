from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import LoginSerializer, UsuarioSerializer, PlanetaSerializer
from rest_framework.generics import ListCreateAPIView
from .models import Usuario, Planeta
from .permissions import IsHumano
from rest_framework.permissions import IsAuthenticated

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

class UsuarioListCreateAPIView(ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsHumano]

class PlanetaListCreateAPIView(ListCreateAPIView):
    queryset = Planeta.objects.all()
    serializer_class = PlanetaSerializer
    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsHumano()]