from django.urls import path
from pedidos import views
from .views import MeusPedidosListView

urlpatterns = [
    path('add/', views.PedidoCreateView.as_view(), name='addpedido'),
    path('resumo/', views.ResumoPedidoTemplateView.as_view(),
         name='resumopedido'),
    path('meus-pedidos/', MeusPedidosListView.as_view(), name='meus_pedidos'),
]