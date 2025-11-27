from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.urls import include
from Manutencoes import views as manutencao_views
from Setores import views as Setores_views
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from Equipamentos.api.viewsets import EquipamentoViewSet
from Manutencoes.api.viewsets import OrdemManutencaoViewSet, PecasManutencaoViewSet
from Pecas.api.viewsets import PecaViewSet
from Setores.api.viewsets import SetorViewSet, EquipamentoSetorViewSet
from Tecnicos.api.viewsets import TecnicoViewSet

router = routers.DefaultRouter()
router.register(r'equipamentos', EquipamentoViewSet)
router.register(r'ordem_manutencao', OrdemManutencaoViewSet)
router.register(r'pecas_manutencao', PecasManutencaoViewSet)
router.register(r'pecas', PecaViewSet)
router.register(r'setores', SetorViewSet)
router.register(r'equipamento_setor', EquipamentoSetorViewSet)
router.register(r'tecnicos', TecnicoViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="Gerenciamento de Equipamentos API",
      default_version='v1',
      description="Trabalho Final WEB II - API para Gerenciamento de Equipamentos e Manutenções",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    # URLs do sistema
    path('', include('Equipamentos.urls')), 
    path('equipamentos/', include('Equipamentos.urls')),
    path('tecnicos/', include('Tecnicos.urls')),
    path('pecas/', include('Pecas.urls')),
    path('manutencoes/', include('Manutencoes.urls')),
    path('setores/', include('Setores.urls')),
    path('accounts/', include('accounts.urls')),

    
    # Gerenciar Equipamentos nos Setores
    path('gerenciar_setor_equipamento/', Setores_views.gerenciar_setor_equipamento, name='gerenciar_setor_equipamento'),
    path('delete_setor_equipamento/<int:id>/', Setores_views.delete_setor_equipamento, name='delete_setor_equipamento'),
    
    # Gerenciar Pecas de Manutencao
    path('gerenciar_pecas_manutencao/', manutencao_views.gerenciar_pecas_manutencao, name='gerenciar_pecas_manutencao'),
    path('delete_pecas_manutencao/<int:id>/', manutencao_views.delete_peca_manutencao, name='delete_pecas_manutencao'),
    
    # URLs de autenticação
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # Documentação da API
    path('api/', include(router.urls)),

    path('api/swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # URLs para JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]