from django.db import models

# Create your models here.

class Livros(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    ano_publicacao = models.DateTimeField(auto_now=True)
    descricao = models.CharField(max_length=500)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name_plural = 'Livros'