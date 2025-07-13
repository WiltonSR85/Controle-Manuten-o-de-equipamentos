from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Tecnico
from .forms import TecnicoForm

def listar_tecnicos(request):
    tecnicos = Tecnico.objects.all()

    return render(request, 'tecnicos/listar_tecnicos.html', {'tecnicos': tecnicos} )

def detalhe_tecnico(request, id):
    tecnico = Tecnico.objects.get(id=id)

    return render(request, 'tecnicos/detalhe_tecnico.html', {'tecnico': tecnico})

def criar_tecnico(request):

    form = TecnicoForm()
    if request.method == 'POST':
        form = TecnicoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/tecnicos/')
    else:
        form = TecnicoForm()

    return render(request, 'tecnicos/form.html', {'form': form})


def edit_tecnico(request, id):

    tecnico = Tecnico.objects.get(id=id)
    form = TecnicoForm(instance=tecnico)

    if request.method == 'POST':
        form = TecnicoForm(request.POST, instance=tecnico)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/tecnicos/')
    else:
        form = TecnicoForm(instance=tecnico)

    return render(request, 'tecnicos/form.html', {'form': form})

def delete_tecnico(request, id):

    tecnico = Tecnico.objects.get(id=id)
    tecnico.delete()
    return HttpResponseRedirect('/tecnicos/')
