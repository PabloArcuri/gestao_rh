from turtle import home
from unicodedata import name
from django.urls import path, include
from .views import DocumentoCreate #, DocumentoDelete

urlpatterns = [
    #path('delete/<pk>', DocumentoDelete.as_view(), name='delete_documento'),
    path('novo/<int:funcionario_id>', DocumentoCreate.as_view(), name='create_document'),
    
]