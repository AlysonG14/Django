from django.db import models

# Create your models here.

class Ecommerce(models.Model):
    number = models.IntegerField()
    titulo = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    image = models.ImageField(upload_to=None, max_length= 100)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __int__(self):
        return self.number

