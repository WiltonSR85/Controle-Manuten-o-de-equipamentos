from django.urls import path
from Setores import views as Setores_views
from .views import SetorListView, SetorDetailView, SetorCreateView, SetorUpdateView, SetorDeleteView

urlpatterns = [
    path('', SetorListView.as_view(), name='listar_setores'),
    path('<int:pk>/', SetorDetailView.as_view(), name='detalhe_setor'),
    path('editsetor/<int:pk>/', SetorUpdateView.as_view(), name='edit_setor'),
    path('criar_setor/', SetorCreateView.as_view(), name='criar_setor'),
    path('deletesetor/<int:pk>/', SetorDeleteView.as_view(), name='delete_setor'),
]
