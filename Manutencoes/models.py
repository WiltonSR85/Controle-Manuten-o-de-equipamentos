from django.db import models
from Equipamentos.models import Equipamento
from Tecnicos.models import Tecnico

class OrdemManutencao(models.Model):
    TIPO_CHOICES = [
        ("Preventiva", "Preventiva"),
        ("Corretiva", "Corretiva"),
    ]

    STATUS_CHOICES = [
        ("Pendente", "Pendente"),
        ("Em andamento", "Em andamento"),
        ("Concluida", "Concluída"),
    ]

    numero_ordem       = models.CharField("Número da Ordem", max_length=20, unique=True, blank=True)
    data_solicitacao   = models.DateField("Data da Solicitação", auto_now_add=True)
    tipo               = models.CharField("Tipo", max_length=10, choices=TIPO_CHOICES)
    descricao_problema = models.TextField("Descrição do Problema")
    status             = models.CharField("Status", max_length=12, choices=STATUS_CHOICES, default="Pendente")
    equipamento        = models.ForeignKey(
        Equipamento,
        on_delete=models.CASCADE,
        related_name="ordens_manutencao"
    )
    tecnico_responsavel = models.ForeignKey(
        Tecnico,
        on_delete=models.CASCADE,
        related_name="ordens_manutencao"
    )

    class Meta:
        ordering = ["-data_solicitacao"]
        verbose_name = "Ordem de Manutenção"
        verbose_name_plural = "Ordens de Manutenção"

    def save(self, *args, **kwargs):
        creating = self.pk is None
        super().save(*args, **kwargs)
        if creating and not self.numero_ordem:
            self.numero_ordem = f"OM-{self.pk:04d}"
            super().save(update_fields=["numero_ordem"])

    def __str__(self):
        return f"{self.numero_ordem} – {self.get_tipo_display()} ({self.get_status_display()})"


class PecasManutencao(models.Model):
    ordem_manutencao = models.ForeignKey(
        OrdemManutencao,
        on_delete=models.CASCADE,
        related_name="pecas"
    )
    peca = models.ForeignKey('Pecas.Peca', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('ordem_manutencao', 'peca')
        verbose_name = "Peça de Manutenção"
        verbose_name_plural = "Peças de Manutenção"
    
    def __str__(self):
        return f"{self.peca}"
