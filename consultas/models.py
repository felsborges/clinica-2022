from django.db import models

# O medelo (models) trata-se de uma classe que extende models.Model
# Este modelo já possui diversos recursos para o uso de banco de dados e interface, 
#   como atribui id, que cria um identificar únido para o registro e o objects, que
#   trata modulo manage que nos possibilita criar comando de consulta no banco de dados

# Documentação para selecionar os Fields
#   https://docs.djangoproject.com/en/4.1/ref/models/fields/
class Especialidade(models.Model):
    # Foi definido que o código da especialidade poderá ser somente
    #   números inteiros positivos, para isso foi utilizado o PositiveIntegerField
    codigo = models.PositiveIntegerField()

    nome = models.CharField(max_length=255)

    descricao = models.CharField(
        max_length=1000,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.nome

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
    data_nascimento = models.DateField(
        null=True,
        blank=True
    )
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

    # Dentro tipos disponibilizados pelo Model Fields é possível localizar o
    #   tipo ForeignKey (chave estrangeira), sendo assim o proprio DJango se responsabiliza em
    #   estrutura o modelo de dados
    especialidade = models.ForeignKey(
        Especialidade,
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )

    # Função padrão de classe para transformar uma classe em texto
    def __str__(self):
        return self.nome

class Procedimento(models.Model):
    nome = models.CharField(max_length = 255)

    def __str__(self):
        return self.nome

class Consulta(models.Model):
    data = models.DateField()
    laudo = models.TextField(
        null = True,
        blank = True
    )
    medico = models.ForeignKey(
        Medico,
        on_delete = models.PROTECT
    )
    procedimentos = models.ManyToManyField(Procedimento)

    def __str__(self):
        return f'{self.data} - {self.medico.nome}'