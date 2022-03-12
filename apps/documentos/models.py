from pyexpat import model
from django.db import models

class Documento(models.Model):
    descricao = models.CharField(max_length=100)
    

    # class Meta:
    #     verbose_name = _("Documento")
    #     verbose_name_plural = _("Documentos")

    def __str__(self):
        return self.descricao

    def get_absolute_url(self):
        return reverse("Documento_detail", kwargs={"pk": self.pk})
