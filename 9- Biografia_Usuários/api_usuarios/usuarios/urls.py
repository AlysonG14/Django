from django.urls import path
from .views import UsuarioListCreateAPIView, UsuarioRetrieveUpdateDestroyAPIViews, Login
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("usuarios/", UsuarioListCreateAPIView.as_view()),
    path("usuarios/<int:pk>/", UsuarioRetrieveUpdateDestroyAPIViews.as_view()),
    path("logar/", Login.as_view())
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)