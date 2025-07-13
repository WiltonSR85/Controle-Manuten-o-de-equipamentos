from django.contrib import admin
from django.urls import path
from Equipamentos import views as equipamento_views
from Tecnicos import views as tecnico_views
from Pecas import views as peca_views

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
]