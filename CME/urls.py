from django.contrib import admin
from django.urls import path
from Equipamentos import views as equipamento_views
from Tecnicos import views as tecnico_views
from Pecas import views as peca_views
from Manutencoes import views as manutencao_views
from Setores import views as Setores_views


urlpatterns = [
    path('admin/', admin.site.urls),
    # Views de Equipamentos
    path('equipamentos/', equipamento_views.listar_equipamentos, name='listar_equipamentos'),
    path('equipamentos/<int:id>/', equipamento_views.detalhe_equipamento, name='detalhe_equipamento'),
    path('editequipamento/<int:id>/', equipamento_views.edit_equipamento, name='edit_equipamento'), 
    path('criarequipamento/', equipamento_views.criar_equipamento, name='criar_equipamento'), 
    path('deleteequipamento/<int:id>/', equipamento_views.delete_equipamento, name='delete_equipamento'), 
    # Views de Tecnicos
    path('tecnicos/', tecnico_views.listar_tecnicos, name='listar_tecnicos'),
    path('tecnicos/<int:id>/', tecnico_views.detalhe_tecnico, name='detalhe_tecnico'),
    path('edittecnico/<int:id>/', tecnico_views.edit_tecnico, name='edit_tecnico'), 
    path('criartecnico/', tecnico_views.criar_tecnico, name='criar_tecnico'), 
    path('deletetecnico/<int:id>/', tecnico_views.delete_tecnico, name='delete_tecnico'),
    # Views de Pecas
    path('pecas/', peca_views.listar_pecas, name='listar_pecas'),
    path('pecas/<int:id>/', peca_views.detalhe_peca, name='detalhe_peca'),
    path('editarpeca/<int:id>/', peca_views.edit_peca, name='edit_peca'), 
    path('criarpeca/', peca_views.criar_peca, name='criar_peca'), 
    path('deletepeca/<int:id>/', peca_views.delete_peca, name='delete_peca'),
    # Views de Manutencoes
    path('manutencoes/', manutencao_views.listar_manutencoes, name='listar_manutencoes'),
    path('manutencoes/<int:id>/', manutencao_views.detalhe_manutencao, name='detalhe_manutencao'),
    path('editmanutencao/<int:id>/', manutencao_views.edit_manutencao, name='edit_manutencao'),
    path('criar_manutencao/', manutencao_views.criar_manutencao, name='criar_manutencao'),
    path('deletemanutencao/<int:id>/', manutencao_views.delete_manutencao, name='delete_manutencao'),
    # Views de Setores
    path('setores/', Setores_views.listar_setores, name='listar_setores'),
    path('setores/<int:id>/', Setores_views.detalhe_setor, name='detalhe_setor'),
    path('editsetor/<int:id>/', Setores_views.edit_setor, name='edit_setor'),
    path('criar_setor/', Setores_views.criar_setor, name='criar_setor'),
    path('deletesetor/<int:id>/', Setores_views.delete_setor, name='delete_setor'),
    # Gerenciar Equipamentos nos Setores
    path('gerenciar_setor_equipamento/', Setores_views.gerenciar_setor_equipamento, name='gerenciar_setor_equipamento'),
    path('gerenciar_equipamentos_setor/<int:id>/', Setores_views.detalhe_setor, name='detalhe_equipamento_setor'),
    # Gerenciar Pecas de Manutencao
    path('gerenciar_pecas_manutencao/', manutencao_views.gerenciar_pecas_manutencao, name='gerenciar_pecas_manutencao'),
    path('gerenciar_pecas_manutencao/<int:id>/', manutencao_views.detalhe_manutencao, name='gerenciar_pecas_manutencao'),
    # Redirect root URL to equipamentos list
    path('', equipamento_views.listar_equipamentos, name='home'),  # Redirect to equipamentos
]