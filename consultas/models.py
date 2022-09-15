from django.db import models

# O medelo (models) trata-se de uma classe que extende models.Model
# Este modelo já possui diversos recursos para o uso de banco de dados e interface, 
#   como atribui id, que cria um identificar únido para o registro e o objects, que
#   trata modulo manage que nos possibilita criar comando de consulta no banco de dados

# Documentação para selecionar os Fields
#   https://docs.djangoproject.com/en/4.1/ref/models/fields/
class Medico(models.Model):
    # CharField: este tipo de atributo cria no banco de dados um campo de texto (VARCHAR)
    #   É obrigatório a parametrização do tamanho máximo, para isso utilizamos o max_length
    nome = models.CharField(max_length=255)
    # Por padrão não é aceito informações nulas nos atributos, para que não sejo obrigatório
    #   o uso de determido atribuito é utilizado o parâmetro null para que no banco de dados
    #   seja no NOT NULL e blank para permitir informações em branco na interface
    cpf = models.CharField(
        max_length=11,
        null=True,
        blank=True
    )
    crm = models.CharField(
        max_length=10,
        null=True,
        blank=True
    )
    # DateField: tipo do atributo que representa uma data
    data_nascimento = models.DateField()
    cidade = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    # EmailField: é o tipo que representa um e-mail.
    #   Para o banco de dados é simplesmente um texto, e para a interface um componente
    #   com validação do e-mail
    email = models.EmailField(
        null=True,
        blank=True
    )
