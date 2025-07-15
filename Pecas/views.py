from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Peca
from .forms import PecaForm

@login_required
def listar_pecas(request):
    pecas = Peca.objects.all()

    return render(request, 'pecas/listar_pecas.html', {'pecas': pecas})

@login_required
def detalhe_peca(request, id):
    peca = Peca.objects.get(id=id)

    return render(request, 'pecas/detalhe_peca.html', {'peca': peca})

@login_required
def criar_peca(request):

    form = PecaForm()
    if request.method == 'POST':
        form = PecaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/pecas/')
    else:
        form = PecaForm()

    return render(request, 'pecas/form.html', {'form': form})

@login_required
def edit_peca(request, id):

    peca = Peca.objects.get(id=id)
    form = PecaForm(instance=peca)

    if request.method == 'POST':
        form = PecaForm(request.POST, instance=peca)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/pecas/')
    else:
        form = PecaForm(instance=peca)

    return render(request, 'pecas/form.html', {'form': form})

@login_required
def delete_peca(request, id):

    peca = Peca.objects.get(id=id)
    peca.delete()
    return HttpResponseRedirect('/pecas/')
