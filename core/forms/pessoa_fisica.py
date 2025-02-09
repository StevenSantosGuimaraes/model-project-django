from django import forms

from core.models.pessoa_fisica import PessoaFisica


class PessoaFisicaForm(forms.ModelForm):
    class Meta:
        model = PessoaFisica
        fields = '__all__'
