from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Planeta(models.Model):
    nome = models.CharField(max_length=50)
    atmosfera = models.BooleanField()
    plantas = models.CharField(max_length=150)
    cor = models.CharField(max_length=10)
    tem_agua = models.BooleanField()
    habitavel = models.BooleanField()
    foto = models.ImageField(upload_to='images/', blank=True, null=True)

class Usuario(AbstractUser):
    especie_escolhas = [
        ('E', 'Experimentos'),
        ('H', 'Humano'),
        ('A', 'Alien')
    ]
    especie = models.CharField(max_length=1, choices=especie_escolhas, default='E')
    idade = models.PositiveIntegerField(blank=True, null=True)
    planeta = models.ForeignKey(Planeta, on_delete=models.CASCADE)
    cor = models.CharField(max_length=15, blank=True, null=True)
    foto = models.ImageField(upload_to='images/', blank=True, null=True)