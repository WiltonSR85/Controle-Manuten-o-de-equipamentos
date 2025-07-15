from django.urls import path
from Pecas import views as peca_views

urlpatterns = [
    path('', peca_views.listar_pecas, name='listar_pecas'),
    path('<int:id>/', peca_views.detalhe_peca, name='detalhe_peca'),
    path('editarpeca/<int:id>/', peca_views.edit_peca, name='edit_peca'), 
    path('criarpeca/', peca_views.criar_peca, name='criar_peca'), 
    path('deletepeca/<int:id>/', peca_views.delete_peca, name='delete_peca'),
]
