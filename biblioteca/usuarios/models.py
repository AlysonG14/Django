from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# criando um modelo de usuário personalizado estendendo o AbstractUser

class UserAbs(AbstractUser):
    # adiciona um campo para armazenar o telefone dentro do usuário
    telefone = models.CharField(max_length=15, blank=True, null=True)

    # blank -> Permite que o campo seja deixado em branco 
    # null -> Permite valores nulos no banco de dados

    # defina a apresentação em string em objeto, retornando em nome do usuário
    def __str__(self):
        return self.username