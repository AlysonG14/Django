from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UserAbs(AbstractUser):
    telefone = models.PositiveIntegerField(blank=True, null=True)
    cargo = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.username
