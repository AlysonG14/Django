from django.db import models

# Create your models here.

class Categoria(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Evento(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    data_hora = models.DateTimeField()
    local = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome}'
    class Meta:
        verbose_name_plural = "Eventos"
