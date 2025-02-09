from django.db import models


class Pessoa(models.Model):
    is_fisica = models.BooleanField()
    
    def __str__(self):

        from .pessoa_fisica import PessoaFisica
        from .pessoa_juridica import PessoaJuridica

        if self.is_fisica:
            pessoa_fisica = PessoaFisica.objects.get(pessoa=self)
            return f"{pessoa_fisica.nome_completo} (CPF: {pessoa_fisica.cpf})"
        else:
            pessoa_juridica = PessoaJuridica.objects.get(pessoa=self)
            return f"{pessoa_juridica.razao_social} (CNPJ: {pessoa_juridica.cnpj})"
