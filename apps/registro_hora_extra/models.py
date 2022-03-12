from xml.parsers.expat import model
from django.db import models


class RegistroHoraExtra(models.Model):
    motivo = models.CharField(max_length=100)
    

    # class Meta:
    #     verbose_name = _("Registro_hora_extra")
    #     verbose_name_plural = _("Registro_hora_extras")

    def __str__(self):
        return self.motivo

    def get_absolute_url(self):
        return reverse("Registro_hora_extra_detail", kwargs={"pk": self.pk})
