from django.urls import path
from .views import UsuarioListCreateAPIVoew, UsuarioRetrieveUpdateDestroyAPIViews, LoginView2 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("usuarios/", UsuarioListCreateAPIVoew.as_view(), name='usuario-list-create'),
    path("usuarios/<int:pk>/", UsuarioRetrieveUpdateDestroyAPIViews.as_view(), name='usuario-específico'),
    path("logar/", LoginView2.as_view(), name='logar')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)