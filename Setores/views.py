from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from .models import Setor
from .forms import SetorForm
from Setores.models import EquipamentoSetor
from .forms import EquipamentoSetorForm
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy

class SetorListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model= Setor
    template_name = 'setores/listar_setores.html'
    context_object_name= 'setores'
    permission_required = 'Setores.view_setor'
    raise_exception = False
    

class SetorDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model= Setor
    template_name = 'setores/detalhe_setor.html'
    context_object_name= 'setor'
    permission_required = 'Setores.view_setor'
    raise_exception = False

class SetorCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model= Setor
    form_class = SetorForm
    template_name = 'setores/form.html'
    permission_required = 'Setores.add_setor'
    success_url = reverse_lazy('listar_setores')

class SetorUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model= Setor
    form_class = SetorForm
    template_name = 'setores/form.html'
    permission_required = 'Setores.change_setor'
    success_url = reverse_lazy('listar_setores')

class SetorDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model= Setor
    template_name = 'setores/confirmar_exclusao.html'
    context_object_name = 'setor'
    permission_required = 'Setores.delete_setor'
    success_url = reverse_lazy('listar_setores')

@login_required
@permission_required('Setores.add_equipamentosetor', raise_exception=False)
@permission_required('Setores.view_equipamentosetor', raise_exception=False)
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
@permission_required('Setores.delete_equipamentosetor', raise_exception=False)
def delete_setor_equipamento(request, id):
    equipamento_setor = EquipamentoSetor.objects.get(id=id)
    equipamento_setor.delete()
    return HttpResponseRedirect(reverse('gerenciar_setor_equipamento'))