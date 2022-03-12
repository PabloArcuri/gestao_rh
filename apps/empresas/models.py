from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import CharField

# Create your models here.
class Empresa(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome da empresa')
            
