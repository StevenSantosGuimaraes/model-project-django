from django.shortcuts import render

from crm.models import Cliente


def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'listar_clientes.html', {'clientes': clientes})
