from django.urls import path
from Tecnicos import views as tecnico_views

urlpatterns = [
   path('', tecnico_views.listar_tecnicos, name='listar_tecnicos'),
    path('<int:id>/', tecnico_views.detalhe_tecnico, name='detalhe_tecnico'),
    path('edittecnico/<int:id>/', tecnico_views.edit_tecnico, name='edit_tecnico'), 
    path('criartecnico/', tecnico_views.criar_tecnico, name='criar_tecnico'), 
    path('deletetecnico/<int:id>/', tecnico_views.delete_tecnico, name='delete_tecnico'),
]
