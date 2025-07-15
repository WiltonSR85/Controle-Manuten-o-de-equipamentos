from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.urls import include
from Manutencoes import views as manutencao_views
from Setores import views as Setores_views


urlpatterns = [
    path('admin/', admin.site.urls),
    # URLs do sistema
    # path('', include('Equipamentos.urls')), 
    path('equipamentos/', include('Equipamentos.urls')),
    path('tecnicos/', include('Tecnicos.urls')),
    path('pecas/', include('Pecas.urls')),
    path('manutencoes/', include('Manutencoes.urls')),
    path('setores/', include('Setores.urls')),
    # Gerenciar Equipamentos nos Setores
    path('gerenciar_setor_equipamento/', Setores_views.gerenciar_setor_equipamento, name='gerenciar_setor_equipamento'),
    path('gerenciar_equipamentos_setor/<int:id>/', Setores_views.detalhe_setor, name='detalhe_equipamento_setor'),
    # Gerenciar Pecas de Manutencao
    path('gerenciar_pecas_manutencao/', manutencao_views.gerenciar_pecas_manutencao, name='gerenciar_pecas_manutencao'),
    path('gerenciar_pecas_manutencao/<int:id>/', manutencao_views.detalhe_manutencao, name='gerenciar_pecas_manutencao'),
    
    # URLs de autenticação
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]