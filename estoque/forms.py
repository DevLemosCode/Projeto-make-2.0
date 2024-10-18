from django import forms
from .models import ItemEstoque


class ItemEstoqueForm(forms.ModelForm):
    class Meta:
        model = ItemEstoque
        fields = ['nome', 'quantidade', 'data_entrega', 'custo_unitario']
        widgets = {
            'data_entrega': forms.DateInput(attrs={'type': 'date'}),
        }
