from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from .models import Setor
from .forms import SetorForm
from Setores.models import EquipamentoSetor
from .forms import EquipamentoSetorForm
from django.urls import reverse

@login_required
@permission_required('Setores.view_setor', raise_exception=True)
def listar_setores(request):
    setores = Setor.objects.prefetch_related('equipamentosetor_set__equipamento').all()
    return render(request, 'setores/listar_setores.html', {'setores': setores})
    
@login_required
@permission_required('Setores.view_setor', raise_exception=True)
def detalhe_setor(request, id):
    setor = Setor.objects.get(id=id)
    return render(request, 'setores/detalhe_setor.html', {'setor': setor})

@login_required
@permission_required('Setores.add_setor', raise_exception=True)
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

@login_required
@permission_required('Setores.change_setor', raise_exception=True)
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

@login_required
@permission_required('Setores.delete_setor', raise_exception=True)
def delete_setor(request, id):
    setor = Setor.objects.get(id=id)
    setor.delete()
    return HttpResponseRedirect('/setores/')

@login_required
@permission_required('Setores.add_equipamentosetor', raise_exception=True)
@permission_required('Setores.view_equipamentosetor', raise_exception=True)
def gerenciar_setor_equipamento(request):
    equipamentos_setores = EquipamentoSetor.objects.select_related('equipamento', 'setor').all()
    form = EquipamentoSetorForm()
    
    if request.method == 'POST':
        form = EquipamentoSetorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('gerenciar_setor_equipamento')) 
            
    return render(request, 'setores/gerenciar_setor_equipamento.html', {
        'equipamentos_setores': equipamentos_setores,
        'form': form
    })

@login_required
@permission_required('Setores.delete_equipamentosetor', raise_exception=True)
def delete_setor_equipamento(request, id):
    equipamento_setor = EquipamentoSetor.objects.get(id=id)
    equipamento_setor.delete()
    return HttpResponseRedirect(reverse('gerenciar_setor_equipamento'))