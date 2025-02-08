from django.urls import path
from .views import listar_pedidos


urlpatterns = [
    path("pedidos/", listar_pedidos, name="listar_pedidos"),
]
