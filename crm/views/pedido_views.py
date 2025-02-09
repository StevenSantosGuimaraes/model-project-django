from django.shortcuts import render

from crm.models.pedido import Pedido


def listar_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, "pedidos.html", {"pedidos": pedidos})
