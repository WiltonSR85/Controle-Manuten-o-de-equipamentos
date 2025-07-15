from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import OrdemManutencao
from .forms import OrdemManutencaoForm
from .models import PecasManutencao
from .forms import PecasManutencaoForm
from django.urls import reverse

@login_required
def listar_manutencoes(request):
    manutencoes = OrdemManutencao.objects.select_related("equipamento").all().order_by("-data_solicitacao")
    return render(request, 'manutencao/listar_manutencao.html', {'manutencoes': manutencoes} )

@login_required
def detalhe_manutencao(request, id):
    manutencao = OrdemManutencao.objects.get(id=id)
    return render(request, 'manutencao/detalhe_manutencao.html', {'manutencao': manutencao} )

@login_required
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
def delete_manutencao(request, id):
    
    manutencao= OrdemManutencao.objects.get(id=id)
    manutencao.delete()
    return HttpResponseRedirect('/manutencoes/')

@login_required
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
