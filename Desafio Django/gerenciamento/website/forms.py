from django import forms
from gerenciamento.models import Funcionario

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ["nome", "sobrenome", "cpf", "tempo_de_servico", "remuneracao"]
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "sobrenome": forms.TextInput(attrs={"class": "form-control"}),
            "cpf": forms.TextInput(attrs={"class": "form-control"}),
            "tempo_de_servico": forms.NumberInput(attrs={"class": "form-control"}),
            "remuneracao": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
        }
