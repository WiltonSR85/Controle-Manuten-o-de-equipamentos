from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required, permission_required

@login_required
@permission_required('accounts.view_user', raise_exception=False)
def listar_usuarios(request):
    usuarios= User.objects.all()
    return render(request  , 'accounts/listar_usuarios.html', {'usuarios': usuarios})
    

@login_required
@permission_required('accounts.view_user', raise_exception=False)
def criar_usuario(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
    else:
        form = CustomUserCreationForm()  

    return render(request, 'accounts/criar_usuario.html', {'form': form})


@login_required
@permission_required('accounts.view_user', raise_exception=False)
def editar_usuario(request, user_id): 
    usuario = get_object_or_404(User, pk=user_id)

    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
    else:
        form = CustomUserChangeForm(instance=usuario)

    return render(request, 'accounts/editar_usuario.html', {'form': form})


@login_required
@permission_required('accounts.view_user', raise_exception=False)
def excluir_usuario(request, user_id):
    usuario = get_object_or_404(User, pk=user_id)

    if request.method == 'POST':
        usuario.delete()
        return redirect('listar_usuarios')

    return render(request, 'accounts/confirmar_exclusao.html', {'usuario': usuario})