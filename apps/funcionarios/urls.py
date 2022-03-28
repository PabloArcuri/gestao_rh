from turtle import home
from unicodedata import name
from django.urls import path, include
from .views import FuncionariosList, FuncionarioEdit, FuncionarioDelete, FuncionarioNovo

urlpatterns = [
    path('', FuncionariosList.as_view(), name='list_funcionarios'),
    path('editar/<pk>', FuncionarioEdit.as_view(), name='update_funcionario'),
    path('delete/<pk>', FuncionarioDelete.as_view(), name='delete_funcionario'),
    path('novo/', FuncionarioNovo.as_view(), name='create_funcionario'),
    
]