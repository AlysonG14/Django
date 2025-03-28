from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.

class Usuario(AbstractUser):
    nome = models.CharField(max_length=255)
    idade = models.PositiveIntegerField()
    telefone = models.PositiveIntegerField()

    groups = models.ManyToManyField(Group, )




