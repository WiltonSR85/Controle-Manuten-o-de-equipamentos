from django.db import models

class Tecnico(models.Model):
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)
    contato = models.CharField(max_length=100)  
    certificacoes = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome} ({self.especialidade})"

