from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
    nome = models.CharField(max_length=255)
    idade = models.PositiveIntegerField(null=True, blank=True)
    telefone = models.CharField(max_length=100)    
    endereco = models.CharField(max_length=255)

    def __str__(self):
        return self.username


