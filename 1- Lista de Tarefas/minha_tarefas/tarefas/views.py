from django.shortcuts import render
from .models import Tarefa

# Create your views here.

def lista_tarefas(request):
    todolist = Tarefa.objects.all().order_by('data_criacao')
    return render(request, 'tarefas/lista_tarefas.html', {'todolist': todolist})

