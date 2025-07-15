from django.urls import path
from Setores import views as Setores_views

urlpatterns = [
    path('', Setores_views.listar_setores, name='listar_setores'),
    path('<int:id>/', Setores_views.detalhe_setor, name='detalhe_setor'),
    path('editsetor/<int:id>/', Setores_views.edit_setor, name='edit_setor'),
    path('criar_setor/', Setores_views.criar_setor, name='criar_setor'),
    path('deletesetor/<int:id>/', Setores_views.delete_setor, name='delete_setor'),
]
