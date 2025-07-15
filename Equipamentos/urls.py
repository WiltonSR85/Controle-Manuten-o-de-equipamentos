from django.contrib import admin
from django.urls import path
from Equipamentos import views as equipamento_views

urlpatterns = [
    path('', equipamento_views.listar_equipamentos, name='listar_equipamentos'),
    path('<int:id>/', equipamento_views.detalhe_equipamento, name='detalhe_equipamento'),
    path('editequipamento/<int:id>/', equipamento_views.edit_equipamento, name='edit_equipamento'), 
    path('criarequipamento/', equipamento_views.criar_equipamento, name='criar_equipamento'), 
    path('deleteequipamento/<int:id>/', equipamento_views.delete_equipamento, name='delete_equipamento'), 
]
