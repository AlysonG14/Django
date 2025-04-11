from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Pato(models.Model):
    nome = models.CharField(max_length=255)
    especie = models.CharField(max_length=255)
    idade = models.PositiveIntegerField()
    peso = models.FloatField()
    cor = models.CharField(max_length=50)
    superPoder = models.CharField(max_length=20)
    cagaTorrada = models.BooleanField(null=True, blank=True)

    def __str__(self):
        if self.cagaTorrada:
            return f'{self.nome} caga torradas perfeitas'
        return f'{self.nome} não caga torradas perfeitas'
    
class DonoDoPato(AbstractUser):
    nome = models.CharField(max_length=10, blank=True, null=True)
    foto_de_perfil = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.username
    

