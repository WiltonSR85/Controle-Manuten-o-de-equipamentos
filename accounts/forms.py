from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label='Email',
        help_text='Obrigatório. Informe um endereço de e-mail válido.',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite o e-mail'
        })
    )

    username = forms.CharField(
        label='Nome de usuário',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite o nome de usuário'
        })
    )

    first_name = forms.CharField(
        label='Primeiro nome',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite o primeiro nome'
        })
    )

    last_name = forms.CharField(
        label='Sobrenome',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite o sobrenome'
        })
    )

    password1 = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite a senha'
        }),
        help_text=UserCreationForm().fields['password1'].help_text  
    )

    password2 = forms.CharField(
        label='Confirme sua senha',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirme a senha'
        }),
        help_text=UserCreationForm().fields['password2'].help_text
    )

    # Adiciona o campo grupo
    grupo = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        required=True,
        label='Grupo',
        widget=forms.Select(attrs={
            'class': 'form-control'
        }),
        help_text='Selecione o grupo para o usuário'
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'grupo']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            grupo = self.cleaned_data['grupo']
            grupo.user_set.add(user)
        return user


class CustomUserChangeForm(UserChangeForm):
    password = None  # Oculta o campo de senha

    username = forms.CharField(
        label='Nome de usuário',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nome de usuário'
        })
    )

    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'E-mail'
        })
    )

    first_name = forms.CharField(
        label='Primeiro nome',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Primeiro nome'
        })
    )

    last_name = forms.CharField(
        label='Sobrenome',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Sobrenome'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
