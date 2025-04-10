from django.db import models


# Create your models here.

class Livro(models.Model):
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=30)
    paginas = models.IntegerField()

def __str__(self):
    return self.titulo

