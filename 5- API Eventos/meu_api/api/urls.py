from django.urls import path
from . import views

urlpatterns = [
    path('eventos/', views.lista_evento),
    path('eventos/<int:pk>/', views.detalhe_evento),
    path('eventos/criar/', views.criar_evento),
    path('eventos/atualizar/<int:pk>/', views.atualizar_evento),
    path('eventos/deletar/<int:pk>/', views.deletar_evento),
    path('eventos/proximos', views.proximo_evento)
]

