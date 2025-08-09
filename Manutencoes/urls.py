from django.urls import path
from Manutencoes import views as manutencao_views
from .views import ManutencaoListView, ManutencaoDetailView, ManutencaoCreateView, ManutencaoUpdateView, ManutencaoDeleteView

urlpatterns = [
    path('', ManutencaoListView.as_view(), name='listar_manutencoes'),
    path('<int:pk>/', ManutencaoDetailView.as_view(), name='detalhe_manutencao'),
    path('editmanutencao/<int:pk>/', ManutencaoUpdateView.as_view(), name='edit_manutencao'),
    path('criar_manutencao/', ManutencaoCreateView.as_view(), name='criar_manutencao'),
    path('deletemanutencao/<int:pk>/', ManutencaoDeleteView.as_view(), name='delete_manutencao'),
]
