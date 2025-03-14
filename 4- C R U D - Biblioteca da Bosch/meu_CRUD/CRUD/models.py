from django.db import models

# Create your models here.

class Livros(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    título = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    ano_publicacao = models.DateField(auto_now=True)
    informacoes = models.CharField(max_length=500)
    data_criacao = models.DateTimeField(auto_now_add=True)