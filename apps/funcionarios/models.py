from audioop import reverse
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from apps.departamentos.models import Departamento
from apps.empresas.models import Empresa


class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    departamentos = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=True, blank=True)

    # class Meta:
    #     verbose_name = _("funcionario")
    #     verbose_name_plural = _("funcionarios")

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("list_funcionarios")
