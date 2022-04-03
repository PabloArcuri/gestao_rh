from django.shortcuts import render
from .models import RegistroHoraExtra
from django.views.generic import ListView


class HoraExtraList(ListView):
    model = RegistroHoraExtra

    def get_queryset(self):
        empresa = self.request.user.funcionario.empresa
        queryset = RegistroHoraExtra.objects.filter(funcionario__empresa = empresa)
        return queryset    
    
        
