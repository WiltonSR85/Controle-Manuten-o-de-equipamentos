from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from .models import Peca
from .forms import PecaForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class PecaListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model= Peca
    template_name = 'pecas/listar_pecas.html'
    context_object_name= 'pecas'
    permission_required = 'Pecas.view_peca'
    raise_exception = False

class PecaDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model= Peca
    template_name = 'pecas/detalhe_peca.html'
    context_object_name= 'peca'
    permission_required = 'Pecas.view_peca'
    raise_exception = False

class PecaCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model= Peca
    form_class = PecaForm
    template_name = 'pecas/form.html'
    permission_required = 'Pecas.add_peca'
    success_url = reverse_lazy('listar_pecas')

class PecaUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model= Peca
    form_class = PecaForm
    template_name = 'pecas/form.html'
    permission_required = 'Pecas.change_peca'
    success_url = reverse_lazy('listar_pecas')

@login_required
@permission_required('Pecas.delete_peca', raise_exception=False)
def delete_peca(request, id):

    peca = Peca.objects.get(id=id)
    peca.delete()
    return HttpResponseRedirect('/pecas/')

class PecaDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model= Peca
    template_name = 'pecas/confirmar_exclusao.html'
    context_object_name = 'peca'
    permission_required = 'Pecas.delete_peca'
    success_url = reverse_lazy('listar_pecas')
