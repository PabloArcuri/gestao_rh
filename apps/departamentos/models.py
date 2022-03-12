from django.db import models


class Departamento(models.Model):
    nome = models.CharField(max_length=100)
    

    # class Meta:
    #     verbose_name = _("departamento")
    #     verbose_name_plural = _("departamentos")

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("departamento_detail", kwargs={"pk": self.pk})
