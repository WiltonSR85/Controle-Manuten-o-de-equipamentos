from django.db import models

class Equipamento(models.Model):
    nome = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    numero_serie = models.CharField(max_length=100)  
    fabricante = models.CharField(max_length=100)
    data_aquisicao = models.DateField()
    
    STATUS_CHOICES = [
        ('ativo', 'Ativo'),
        ('inativo', 'Inativo'),
        ('manutencao', 'Em manutenção'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ativo')

    setores = models.ManyToManyField(
        'Setores.Setor',
        through='Setores.EquipamentoSetor',
        related_name='equipamentos'
    )

    def __str__(self):
        return f"{self.nome} ({self.modelo})"

