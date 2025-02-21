from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.name
 
    class Meta:
        verbose_name_plural = "Itens"
        