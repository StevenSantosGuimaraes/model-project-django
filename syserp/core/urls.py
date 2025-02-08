from django.urls import path
from .views import *


urlpatterns = [
    path('clientes/', listar_clientes, name='listar_clientes'),
]
