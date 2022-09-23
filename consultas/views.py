# O módulo views é responsável por conter todas as funções que retornam
#   informações ao usuário
# Para isso também será necessário receber as requisições

# O DJango inclui no código das views por padrão
#   a importação do django.shortcuts.render
# Este módulo é responsável por transforma o template em um html
#   legivel para o navegador
from django.http import HttpResponse
from django.shortcuts import render

from .models import Medico

# Por definição as funções de visualização precisam obrigatoriamente ter
#   um parâmetro de request
def medicos(request):
    # Utilizar o modelo (para este caso Medico) para buscar do banco de dados
    #   todos os médicos
    medicos = Medico.objects.all()

    # Variável do tipo dicionário que será responsável por armazenar o contexto
    #   que será enviado para o template
    contexto = { 'medicos': medicos }

    # Já o retorno será uma resposta HTTP, para isso será necessário utilizar
    #   a função HttpResponse

    # Quando os módulos do shortcut são utilizados é
    #   reduzido o volume de código
    # No caso render, é necessário colocar como primeiro parâmetro
    #   o request, sem segundo o template e por último o contexto
    return render(request, 'medicos.html', contexto)

# Função desenvolvida para fornecer os detalhes do médico, para isso foi necessário que fosse declarado
#   o parâmetro medico_id para receber a informção vinda da URL
def medico_detalhes(request, medico_id):
    # Para todo os modelos é possível utilizar o método .get que tem a função de fazer uma consulta
    #   no banco de dados e retornar somente um item
    # pk -> é um parâmetro possível que faz referência a primary key (chave primária) definida no modelo
    medico = Medico.objects.get(pk=medico_id)

    contexto = { 'medico': medico }

    return render(request, 'medico_detalhes.html', contexto)
