from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from gerenciamento.models import Funcionario
from .forms import FuncionarioForm

class FuncionarioListView(ListView):
    template_name = 'website/lista_funcionarios.html'
    model = Funcionario
    context_object_name = 'funcionarios'


class FuncionarioCreateView(CreateView):
    template_name = 'website/cria_funcionario.html'
    model = Funcionario
    form_class = FuncionarioForm
    success_url = reverse_lazy('website:lista_funcionarios')


class FuncionarioUpdateView(UpdateView):
    template_name = 'website/edita_funcionario.html'
    model = Funcionario
    form_class = FuncionarioForm
    success_url = reverse_lazy('website:lista_funcionarios')


class FuncionarioDeleteView(DeleteView):
    template_name = 'website/exclui_funcionario.html'
    model = Funcionario
    context_object_name = 'funcionario'
    success_url = reverse_lazy('website:lista_funcionarios')
