from django.db import models


class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    

    # class Meta:
    #     verbose_name = _("funcionario")
    #     verbose_name_plural = _("funcionarios")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("funcionario_detail", kwargs={"pk": self.pk})
