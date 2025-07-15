from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from .models import OrdemManutencao
from .forms import OrdemManutencaoForm
from .models import PecasManutencao
from .forms import PecasManutencaoForm
from django.urls import reverse

@login_required
@permission_required('Manutencoes.view_ordemmanutencao', raise_exception=True)
def listar_manutencoes(request):
    manutencoes = OrdemManutencao.objects.select_related("equipamento").all().order_by("-data_solicitacao")
    return render(request, 'manutencao/listar_manutencao.html', {'manutencoes': manutencoes} )

@login_required
@permission_required('Manutencoes.view_ordemmanutencao', raise_exception=True)
def detalhe_manutencao(request, id):
    manutencao = OrdemManutencao.objects.get(id=id)
    return render(request, 'manutencao/detalhe_manutencao.html', {'manutencao': manutencao} )

@login_required
@permission_required('Manutencoes.add_ordemmanutencao', raise_exception=True)
def criar_manutencao(request):
    form = OrdemManutencaoForm()
    if request.method == 'POST':
        form = OrdemManutencaoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/manutencoes/')
    else:
        form = OrdemManutencaoForm()
    
    return render(request, 'manutencao/form.html', {'form': form})

@login_required
@permission_required('Manutencoes.change_ordemmanutencao', raise_exception=True)
def edit_manutencao(request, id):
    manutencao = OrdemManutencao.objects.get(id=id)
    form = OrdemManutencaoForm(instance=manutencao)

    if request.method == 'POST':
        form = OrdemManutencaoForm(request.POST, instance=manutencao)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/manutencoes/')
    else:
        form = OrdemManutencaoForm(instance=manutencao)

    return render(request, 'manutencao/form.html', {'form': form})

@login_required
@permission_required('Manutencoes.delete_ordemmanutencao', raise_exception=True)
def delete_manutencao(request, id):
    
    manutencao= OrdemManutencao.objects.get(id=id)
    manutencao.delete()
    return HttpResponseRedirect('/manutencoes/')

@login_required
@permission_required('Manutencoes.view_pecasmanutencao', raise_exception=True)
@permission_required('Manutencoes.add_pecasmanutencao', raise_exception=True)
@permission_required('Manutencoes.change_pecasmanutencao', raise_exception=True)
def gerenciar_pecas_manutencao(request):
    peca_manutencao = PecasManutencao.objects.select_related('ordem_manutencao', 'peca').all()
    form = PecasManutencaoForm()
    
    if request.method == 'POST':
        form = PecasManutencaoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('gerenciar_pecas_manutencao'))
            
    return render(request, 'manutencao/gerenciar_pecas_manutencao.html', {
        'peca_manutencao': peca_manutencao,
        'form': form
    })

@login_required
@permission_required('Manutencoes.delete_pecasmanutencao', raise_exception=True)
def delete_peca_manutencao(request, id):
    peca_manutencao = PecasManutencao.objects.get(id=id)
    peca_manutencao.delete()
    return HttpResponseRedirect(reverse('gerenciar_pecas_manutencao'))
