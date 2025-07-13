from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Equipamento
from .forms import EquipamentoForm

def listar_equipamentos(request):
    equipamentos= Equipamento.objects.all()

    return render(request, 'equipamentos/listar_equipamentos.html', {'equipamentos': equipamentos} )

def detalhe_equipamento(request, id):
    equipamento = (
        Equipamento.objects
        .prefetch_related('setores')          # ➋  traz todos os setores juntos
        .get(id=id)
    )

    return render(request,
                  'equipamentos/detalhe_equipamento.html',
                  {'equipamento': equipamento})
def criar_equipamento(request):

    form=EquipamentoForm()
    if request.method == 'POST':
        form=EquipamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/equipamentos/')
    else:
        form=EquipamentoForm()
    
    return render(request, 'equipamentos/form.html', {'form': form})


def edit_equipamento(request, id):

    equipamento= Equipamento.objects.get(id=id)
    form=EquipamentoForm(instance=equipamento)

    if request.method == 'POST':
        form=EquipamentoForm(request.POST, instance=equipamento)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/equipamentos/')
    else:
        form=EquipamentoForm(instance=equipamento)

    return render(request, 'equipamentos/form.html', {'form': form})

def delete_equipamento(request, id):
    
    equipamento= Equipamento.objects.get(id=id)
    equipamento.delete()
    return HttpResponseRedirect('/equipamentos/')
