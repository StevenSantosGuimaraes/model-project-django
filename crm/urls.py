from django.urls import path

from .views import * 


urlpatterns = [
    path('clientes/', listar_clientes, name='listar_clientes'),
    #path("pedidos/", listar_pedidos, name="listar_pedidos"),

    path('clientes/cadastrar/', criar_cliente, name='cadastrar_cliente'),

]
