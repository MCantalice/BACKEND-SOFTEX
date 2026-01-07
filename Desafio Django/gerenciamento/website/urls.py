from django.urls import path
from .views import (
    FuncionarioListView,
    FuncionarioCreateView,
    FuncionarioUpdateView,
    FuncionarioDeleteView
)

app_name = 'website'

urlpatterns = [
    path('', FuncionarioListView.as_view(), name='lista_funcionarios'),
    path('funcionario/cadastrar/', FuncionarioCreateView.as_view(), name='cadastra_funcionario'),
    path('funcionario/editar/<int:pk>/', FuncionarioUpdateView.as_view(), name='edita_funcionario'),
    path('funcionario/excluir/<int:pk>/', FuncionarioDeleteView.as_view(), name='exclui_funcionario'),
]
