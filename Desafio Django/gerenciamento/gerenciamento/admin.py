from django.contrib import admin
from .models import Funcionario

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = (
        "nome",
        "sobrenome",
        "cpf",
        "tempo_de_servico",
        "remuneracao",
    )

    search_fields = ("nome", "sobrenome", "cpf")
    list_filter = ("tempo_de_servico",)
