from django.urls import path
from Tecnicos import views as tecnico_views
from .views import TecnicoListView, TecnicoDetailView, TecnicoCreateView, TecnicoUpdateView, TecnicoDeleteView

urlpatterns = [
   path('', TecnicoListView.as_view(), name='listar_tecnicos'),
    path('<int:pk>/', TecnicoDetailView.as_view(), name='detalhe_tecnico'),
    path('edittecnico/<int:pk>/', TecnicoUpdateView.as_view(), name='edit_tecnico'), 
    path('criartecnico/', TecnicoCreateView.as_view(), name='criar_tecnico'), 
    path('deletetecnico/<int:pk>/', TecnicoDeleteView.as_view(), name='delete_tecnico'),
]
