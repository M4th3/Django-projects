from django.shortcuts import render
from .models import Usuario, Cargo
from django.views.generic import CreateView, TemplateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

class CreateUsuario(LoginRequiredMixin, CreateView):
    model = Usuario
    login_url = reverse_lazy('login')
    fields = ['nome', 'idade', 'cpf']
    template_name = 'form.html'
    success_url = reverse_lazy('index')

class CreateCargo(CreateView):
    model = Cargo   
    fields = ['cargo', 'funcao', 'usuario'] 
    template_name = 'form.html'
    success_url = reverse_lazy('index')

class UpdateUsuario(UpdateView):
    model = Usuario
    fields = ['nome', 'idade', 'cpf']
    template_name = 'form.html'
    success_url = reverse_lazy('listusuario')

class UpdateCargo(UpdateView):
    model = Cargo
    fields = ['cargo', 'funcao', 'usuario']
    template_name = 'form.html'
    success_url = reverse_lazy('listcargo')

class DeleteUsuario(DeleteView):
    model = Usuario
    template_name = 'form.html'
    success_url = reverse_lazy('listusuario')

class DeleteCargo(DeleteView):
    model = Cargo
    template_name = 'form.html'        
    success_url = reverse_lazy('listcargo')

class ListUsuario(ListView):
    model = Usuario
    template_name = 'listusuario.html'

class ListCargo(ListView):
    model = Cargo 
    template_name = 'listcargo.html'   

