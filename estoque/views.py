from django.shortcuts import render, redirect
from .models import ItemEstoque
from .forms import ItemEstoqueForm



def registrar_item(request):
    if request.method == 'POST':
        form = ItemEstoqueForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('listar_estoque')
    else:
        form = ItemEstoqueForm()
    return render(request, 'estoque/registrar_item.html', {'form': form})

def listar_estoque(request):
    itens = ItemEstoque.objects.all()
    return render(request, 'estoque/listar_estoque.html', {'itens': itens})
