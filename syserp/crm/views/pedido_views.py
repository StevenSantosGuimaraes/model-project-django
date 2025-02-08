from django.shortcuts import render
from crm.models import Pedido


def listar_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, "vendas/lista_pedidos.html", {"pedidos": pedidos})
