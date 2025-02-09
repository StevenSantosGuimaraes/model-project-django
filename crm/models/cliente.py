from django.db import models

from core.models import Pessoa


class Cliente(models.Model):
    pessoa = models.OneToOneField(Pessoa, on_delete=models.PROTECT)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.pessoa} - {'Ativo' if self.ativo else 'Inativo'}"
