from django.contrib import admin
from django.urls import path
from Equipamentos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('equipamentos/', views.listar_equipamentos, name='listar_equipamentos'),
    path('equipamentos/<int:id>/', views.detalhe_equipamento, name='detalhe_equipamento'),
    path('editequipamento/<int:id>/', views.edit_equipamento, name='edit_equipamento'), 
    path('criarequipamento/', views.criar_equipamento, name='criar_equipamento'), 
    path('deleteequipamento/<int:id>/', views.delete_equipamento, name='delete_equipamento'), 
]