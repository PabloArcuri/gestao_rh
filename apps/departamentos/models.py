from django.urls import reverse
from django.db import models
from apps.empresas.models import Empresa



class Departamento(models.Model):
    nome = models.CharField(max_length=100)
    empresa = models.ForeignKey(Empresa, on_delete=models.SET_NULL, blank=True, null=True)

    # class Meta:
    #     verbose_name = _("departamento")
    #     verbose_name_plural = _("departamentos")

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("list_departamentos")
