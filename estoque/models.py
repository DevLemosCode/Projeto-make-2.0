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

    def enviar_para_webhook(self):
        webhook_url = "https://hook.us2.make.com/pt2ewusxvufcqili77m9r3i2elam0iuu"  
        dados = {
            'nome': self.nome,
            'quantidade': self.quantidade,
            'data_entrega': self.data_entrega.strftime('%Y-%m-%d'),
            'custo_unitario': str(self.custo_unitario),
            'custo_total': str(self.custo_total),
        }

   
        try:
            response = requests.post(webhook_url, json=dados)
            response.raise_for_status()  
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar webhook: {e}")

    def __str__(self):
        return f'{self.nome} - {self.quantidade} unidades'
