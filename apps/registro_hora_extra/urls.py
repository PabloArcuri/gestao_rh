from django.urls import path, include
from .views import HoraExtraList

urlpatterns = [
    path('', HoraExtraList.as_view(), name='list_hora_extra'),
    # path('editar/<pk>', FuncionarioEdit.as_view(), name='update_funcionario'),
    # path('delete/<pk>', FuncionarioDelete.as_view(), name='delete_funcionario'),
    # path('novo/', FuncionarioNovo.as_view(), name='create_funcionario'),
    
]