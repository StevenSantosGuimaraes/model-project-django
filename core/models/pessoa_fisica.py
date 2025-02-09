from django.db import models

from .pessoa import Pessoa


class PessoaFisica(Pessoa):
    nome_completo = models.CharField(max_length=64)
    cpf = models.CharField(max_length=14, unique=True)
    pessoa = models.OneToOneField(Pessoa, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nome_completo} ({self.cpf})"
