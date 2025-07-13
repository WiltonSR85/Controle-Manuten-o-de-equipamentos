from django.db import models

class Peca(models.Model):
    nome_da_peca = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100)
    fabricante = models.CharField(max_length=100)  
    estoque = models.IntegerField()
    data_da_ultima_compra = models.DateField()

    def __str__(self):
        return f"{self.nome_da_peca} ({self.codigo})"

