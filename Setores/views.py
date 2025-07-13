from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Setor
from .forms import SetorForm
from Setores.models import EquipamentoSetor
from .forms import EquipamentoSetorForm
from django.urls import reverse

def listar_setores(request):
    setores = Setor.objects.prefetch_related('equipamentosetor_set__equipamento').all()
    return render(request, 'setores/listar_setores.html', {'setores': setores})
    
def detalhe_setor(request, id):
    setor = Setor.objects.get(id=id)
    return render(request, 'setores/detalhe_setor.html', {'setor': setor})

def criar_setor(request):
    form = SetorForm()
    if request.method == 'POST':
        form = SetorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/setores/')
    else:
        form = SetorForm()
    
    return render(request, 'setores/form.html', {'form': form})

def edit_setor(request, id):
    setor = Setor.objects.get(id=id)
    form = SetorForm(instance=setor)

    if request.method == 'POST':
        form = SetorForm(request.POST, instance=setor)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/setores/')
    else:
        form = SetorForm(instance=setor)

    return render(request, 'setores/form.html', {'form': form})

def delete_setor(request, id):
    setor = Setor.objects.get(id=id)
    setor.delete()
    return HttpResponseRedirect('/setores/')

def gerenciar_setor_equipamento(request):
    equipamentos_setores = EquipamentoSetor.objects.select_related('equipamento', 'setor').all()
    form = EquipamentoSetorForm()
    
    if request.method == 'POST':
        form = EquipamentoSetorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('gerenciar_setor_equipamento')) # Redirecione para a mesma página
            
    return render(request, 'setores/gerenciar_setor_equipamento.html', {
        'equipamentos_setores': equipamentos_setores,
        'form': form
    })