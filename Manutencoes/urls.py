from django.urls import path
from Manutencoes import views as manutencao_views

urlpatterns = [
    path('', manutencao_views.listar_manutencoes, name='listar_manutencoes'),
    path('<int:id>/', manutencao_views.detalhe_manutencao, name='detalhe_manutencao'),
    path('editmanutencao/<int:id>/', manutencao_views.edit_manutencao, name='edit_manutencao'),
    path('criar_manutencao/', manutencao_views.criar_manutencao, name='criar_manutencao'),
    path('deletemanutencao/<int:id>/', manutencao_views.delete_manutencao, name='delete_manutencao'),
]
