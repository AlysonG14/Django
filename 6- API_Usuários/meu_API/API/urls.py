from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    path('api/usuario/', view=views.usuario),
    path('api/usuario/criar', view=views.create_user),
    path('api/usuario/logar', view=views.logar),

    # Aqui descreveremos uma rota de JWT que vai autenticar o tokenrefresh do usuário de login
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh')

]   