from django.db import models
from Tecnicos.models import Tecnico

class Setor(models.Model):
    nome = models.CharField(max_length=100)
    
    tecnico_responsavel = models.ForeignKey(
        Tecnico,
        on_delete=models.CASCADE,
        related_name="setores_responsaveis"
    )

    localizacao = models.CharField(max_length=100)


    class Meta:
        ordering = ['nome']
        verbose_name = 'Setor'
        verbose_name_plural = 'Setores'
        
    def __str__(self):
        return f"{self.nome} ({self.nome})"
    

class EquipamentoSetor(models.Model):
    """
    Tabela de junção para o relacionamento N:N entre Equipamento e Setor.
    """
    equipamento = models.ForeignKey('Equipamentos.Equipamento', on_delete=models.CASCADE)
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)

    class Meta:
        # Garante que um par equipamento-setor seja único
        unique_together = ('equipamento', 'setor')
        verbose_name = "Equipamento no Setor"
        verbose_name_plural = "Equipamentos nos Setores"

    def __str__(self):
        return f"{self.equipamento.nome} - {self.setor.nome}"