from django.urls import path
from .views import PatoListCreateAPIView, PatoRetrieveUpdateDestroyAPIViews, LoginView2
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("patos/", PatoListCreateAPIView.as_view(), name='pato-list-create'),
    path('patos/<int:pk>/', PatoRetrieveUpdateDestroyAPIViews.as_view(), name='pato-especifico'),
    path('logar/', LoginView2.as_view(), name='logar'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    