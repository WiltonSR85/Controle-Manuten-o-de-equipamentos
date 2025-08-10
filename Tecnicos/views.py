from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from .models import Tecnico
from .forms import TecnicoForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class TecnicoListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model= Tecnico
    template_name = 'tecnicos/listar_tecnicos.html'
    context_object_name= 'tecnicos'
    permission_required = 'Tecnicos.view_tecnico'
    raise_exception = True

class TecnicoDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model= Tecnico
    template_name = 'tecnicos/detalhe_tecnico.html'
    context_object_name= 'tecnico'
    permission_required = 'Tecnicos.view_tecnico'
    raise_exception = True

class TecnicoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model= Tecnico
    form_class = TecnicoForm
    template_name = 'tecnicos/form.html'
    permission_required = 'Tecnicos.add_tecnico'
    success_url = reverse_lazy('listar_tecnicos')

class TecnicoUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model= Tecnico
    form_class = TecnicoForm
    template_name = 'tecnicos/form.html'
    permission_required = 'Tecnicos.change_tecnico'
    success_url = reverse_lazy('listar_tecnicos')

class TecnicoDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model= Tecnico
    template_name = 'tecnicos/confirmar_exclusao.html'
    context_object_name = 'tecnico'
    permission_required = 'Tecnicos.delete_tecnico'
    success_url = reverse_lazy('listar_tecnicos')
