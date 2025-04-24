from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

ESCOLARIDADE = [
    ('EI', 'Educação Infantil'),
    ('EF', 'Ensino Fundamental'),
    ('EM', 'Ensino Médio'),
    ('ES', 'Ensino Superior'),
]

               
class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    biografia = models.TextField(max_length=300)
    idade = models.IntegerField(null=True, blank=True)
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=255)
    escolaridade = models.CharField(max_length=2, choices=ESCOLARIDADE, blank=True, null=True)
    animais = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.nome}'
    
class UsuarioAuthenticate(AbstractUser):
    nome = models.CharField(max_length=10, blank=True, null=True)
    idade = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.username
