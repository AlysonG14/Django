from django.db import models

# Create your models here.

class Aluno(models.Model):
    nome = models.CharField(max_length=70)
    idade = models.PositiveIntegerField()
    curso = models.CharField(max_length=50)
    instituicao = models.CharField(max_length=100)
    rm = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nome}-{self.rm}"
    class Meta:
        verbose_name_plural = "Alunos" 