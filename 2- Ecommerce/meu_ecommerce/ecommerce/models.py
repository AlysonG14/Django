from django.db import models

# Create your models here.

class Ecommerce(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to="produtos/")
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __int__(self):
        return self.titulo

