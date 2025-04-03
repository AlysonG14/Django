from django.urls import path
from . import views

urlpatterns = [
    path('livros/', views.lista_livros, name='livros.html'),
    path('api/livros/', views.livros)
]

