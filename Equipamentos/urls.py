from django.contrib import admin
from django.urls import path
from Equipamentos import views as equipamento_views
from .views import EquipamentoListView, EquipamentoDetailView, EquipamentoCreateView, EquipamentoUpdateView, EquipamentoDeleteView

urlpatterns = [
    path('', EquipamentoListView.as_view(), name='listar_equipamentos'),
    path('<int:pk>/', EquipamentoDetailView.as_view(), name='detalhe_equipamento'),
    path('editequipamento/<int:pk>/', EquipamentoUpdateView.as_view(), name='edit_equipamento'), 
    path('criarequipamento/', EquipamentoCreateView.as_view(), name='criar_equipamento'), 
    path('deleteequipamento/<int:pk>/', EquipamentoDeleteView.as_view(), name='delete_equipamento'), 
]
