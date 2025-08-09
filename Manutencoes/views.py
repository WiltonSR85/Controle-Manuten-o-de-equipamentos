from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from .models import OrdemManutencao
from .forms import OrdemManutencaoForm
from .models import PecasManutencao
from .forms import PecasManutencaoForm
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class ManutencaoListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model= OrdemManutencao
    template_name = 'manutencao/listar_manutencao.html'
    context_object_name= 'manutencoes'
    permission_required = 'Manutencoes.view_ordemmanutencao'
    raise_exception = True

class ManutencaoDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model= OrdemManutencao
    template_name = 'manutencao/detalhe_manutencao.html'
    context_object_name= 'manutencao'
    permission_required = 'Manutencoes.view_ordemmanutencao'
    raise_exception = True

class ManutencaoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model= OrdemManutencao
    form_class = OrdemManutencaoForm
    template_name = 'manutencao/form.html'
    permission_required = 'Manutencoes.add_ordemmanutencao'
    success_url = reverse_lazy('listar_manutencoes')

class ManutencaoUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model= OrdemManutencao
    form_class = OrdemManutencaoForm
    template_name = 'manutencao/form.html'
    permission_required = 'Manutencoes.change_ordemmanutencao'
    success_url = reverse_lazy('listar_manutencoes')

class ManutencaoDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = OrdemManutencao
    template_name = 'manutencao/confirmar_exclusao.html'
    context_object_name = 'manutencao'
    permission_required = 'Manutencoes.delete_ordemmanutencao'
    success_url = reverse_lazy('listar_manutencoes')

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
