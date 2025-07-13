from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Peca
from .forms import PecaForm

def listar_pecas(request):
    pecas = Peca.objects.all()

    return render(request, 'pecas/listar_pecas.html', {'pecas': pecas})

def detalhe_peca(request, id):
    peca = Peca.objects.get(id=id)

    return render(request, 'pecas/detalhe_peca.html', {'peca': peca})

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

def delete_peca(request, id):

    peca = Peca.objects.get(id=id)
    peca.delete()
    return HttpResponseRedirect('/pecas/')
