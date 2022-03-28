from dataclasses import fields
from ssl import _create_unverified_context
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from .models import Departamento
from django.urls import reverse_lazy



class DepartamentosList(ListView):
    model = Departamento
    

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Departamento.objects.filter(empresa = empresa_logada)


class DepartamentosCreate(CreateView):
    model = Departamento
    fields = ['nome']

    def form_valid(self, form):
        departamento = form.save(commit = False)
        departamento.empresa = self.request.user.funcionario.empresa
        departamento.save()
        return super(DepartamentosCreate, self).form_valid(form)

class DepartamentosUpdate(UpdateView):
    model = Departamento
    fields = ['nome']

class DepartamentosDelete(DeleteView):
    model = Departamento
    success_url =  reverse_lazy('list_departamentos')    
