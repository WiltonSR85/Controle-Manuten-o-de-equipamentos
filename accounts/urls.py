from django.urls import path
from .views import listar_usuarios, criar_usuario, editar_usuario, excluir_usuario

urlpatterns = [
    path('', listar_usuarios, name='listar_usuarios'),
    path('criar/', criar_usuario, name= 'criar_usuario'),
    path('editar/<int:user_id>/', editar_usuario, name='editar_usuario'),
    path('excluir/<int:user_id>/', excluir_usuario, name= 'excluir_usuario')
]