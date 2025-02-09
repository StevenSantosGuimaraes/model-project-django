from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from crm.models.cliente import Cliente

from crm.forms.cliente import ClienteForm
from core.forms import PessoaFisicaForm, PessoaJuridicaForm


@login_required
def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, "clientes.html", {"clientes": clientes})

@login_required
def criar_cliente(request):
    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST)
        pessoa_fisica_form = PessoaFisicaForm(request.POST)
        pessoa_juridica_form = PessoaJuridicaForm(request.POST)
        if cliente_form.is_valid():
            cliente = cliente_form.save(commit=False)
            if 'cpf' in request.POST:
                if pessoa_fisica_form.is_valid():
                    pessoa = pessoa_fisica_form.save()
            else:
                if pessoa_juridica_form.is_valid():
                    pessoa = pessoa_juridica_form.save()
            cliente.pessoa = pessoa
            cliente.save()
            return redirect('listar_clientes')
    else:
        cliente_form = ClienteForm()
        pessoa_fisica_form = PessoaFisicaForm()
        pessoa_juridica_form = PessoaJuridicaForm()
    return render(request, 'clientes_form.html', {
        'cliente_form': cliente_form,
        'pessoa_fisica_form': pessoa_fisica_form,
        'pessoa_juridica_form': pessoa_juridica_form
    })
