from django import forms

from core.models.pessoa_juridica import PessoaJuridica


class PessoaJuridicaForm(forms.ModelForm):
    class Meta:
        model = PessoaJuridica
        fields = '__all__'
