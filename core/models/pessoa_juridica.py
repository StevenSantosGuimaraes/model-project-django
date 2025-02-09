from django.db import models

from .pessoa import Pessoa


class PessoaJuridica(Pessoa):
    razao_social = models.CharField(max_length=64)
    cnpj = models.CharField(max_length=18, unique=True)
    pessoa = models.OneToOneField(Pessoa, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.razao_social} ({self.cnpj})"
