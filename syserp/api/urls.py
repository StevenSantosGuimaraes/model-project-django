from django.urls import path
from .views import *


urlpatterns = [
    path('clientes/', listar_clientes_api, name='api_listar_clientes'),
    path('clientes/<int:id>/', listar_clientes_api, name='detalhar_cliente'),
]
