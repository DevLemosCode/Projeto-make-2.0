from django.db import models
import requests

class ItemEstoque(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    data_entrega = models.DateField()
    custo_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    custo_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        
        self.custo_total = self.quantidade * self.custo_unitario
        super().save(*args, **kwargs)

        
        self.enviar_para_webhook()

    
    def __str__(self):
        return f'{self.nome} - {self.quantidade} unidades'
