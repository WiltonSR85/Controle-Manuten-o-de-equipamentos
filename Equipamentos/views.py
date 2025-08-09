from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .models import Equipamento
from .forms import EquipamentoForm

class EquipamentoListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model= Equipamento
    template_name = 'equipamentos/listar_equipamentos.html'
    context_object_name= 'equipamentos'
    permission_required = 'Equipamentos.view_equipamento'
    raise_exception = True

class EquipamentoDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Equipamento
    template_name = 'equipamentos/detalhe_equipamento.html'
    context_object_name = 'equipamento'
    permission_required = 'Equipamentos.view_equipamento'
    raise_exception = True

class EquipamentoCreateView( LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Equipamento
    form_class = EquipamentoForm
    template_name = 'equipamentos/form.html'
    permission_required = 'Equipamentos.add_equipamento'
    success_url = reverse_lazy('listar_equipamentos')

class EquipamentoUpdateView( LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Equipamento
    form_class = EquipamentoForm
    template_name = 'equipamentos/form.html'
    permission_required = 'Equipamentos.change_equipamento'
    success_url = reverse_lazy('listar_equipamentos')

class EquipamentoDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Equipamento
    template_name = 'equipamentos/confirmar_exclusao.html'
    context_object_name = 'equipamento'
    permission_required = 'Equipamentos.delete_equipamento'
    success_url = reverse_lazy('listar_equipamentos')
