from django.urls import path
from .views import PecaListView, PecaDetailView, PecaCreateView, PecaUpdateView, PecaDeleteView
urlpatterns = [
    path('', PecaListView.as_view(), name='listar_pecas'),
    path('<int:pk>/', PecaDetailView.as_view(), name='detalhe_peca'),
    path('editarpeca/<int:pk>/', PecaUpdateView.as_view(), name='edit_peca'), 
    path('criarpeca/', PecaCreateView.as_view(), name='criar_peca'), 
    path('deletepeca/<int:pk>/', PecaDeleteView.as_view(), name='delete_peca'),
]
