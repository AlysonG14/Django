from django.db import models

# Create your models here.

    
# Vou criar outra classe chamado: "TO-DO-LIST" para adicionar e registrar pelo admin e por fim colocar adicionar ele no HTML de site.    
class Tarefa(models.Model):
    descricao = models.CharField(max_length=300)
    status = models.BooleanField(blank= False, null=False, default=False)
    data_criacao = models.DateTimeField(auto_now_add=True)
            

    def __str__(self):
        return self.descricao

