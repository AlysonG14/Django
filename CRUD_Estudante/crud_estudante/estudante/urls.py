from django.urls import path
from . import views

urlpatterns = [
    path('alunos/', views.listar_alunos),
    path('alunos/criar/', views.criar_aluno)
]