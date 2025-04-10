from django.db import models

# Create your models here.

CATEGORIA = [
    ("Música", "Música"),
    ("Acampamento", "Acampamento"),
    ("Workshop", "Workshop"),
    ("Palestra", "Palestra")

]

class Evento(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    data_hora = models.DateTimeField()
    local = models.CharField(max_length=255)
    categoria = models.CharField(max_length=11, choices=CATEGORIA, blank=False, null=False)

    def __str__(self):
        return f'{self.nome}'
    class Meta:
        verbose_name_plural = "Eventos"
