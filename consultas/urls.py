# O arquivo urls.py é responsável por tratar o direcionamento das rotas,
#   conforme a requisição do usuário
from unicodedata import name
from django.urls import path

from . import views

# Variável obrigatória
# A variável urlpatterns é uma lista, e a ordem dos itens importam
urlpatterns = [
    # A fução path é resposável por estruturar a rota da aplicação
    path('', views.medicos),
    path('medicos/', views.medicos, name='medicos'),
    path('medicos/cadastro/', views.medico_cadastro, name='medico_cadastro'),
    # Para criar uma URL dinâmica é necessário colocar a parte dinâmica entre < e >, o valor
    #   associado nesta parte da URL será passado por parâmero para a view
    # O DJango fará a seguinte chamada de função para este exemplo
    #   views.medico_detalhes(request=requerst, medico_id=medico_id)
    path('medicos/<medico_id>/detalhes/', views.medico_detalhes, name='medico_detalhes'),
]