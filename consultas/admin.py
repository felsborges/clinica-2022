from django.contrib import admin

# Importar o módulo criado dentro do arquivo models.py
# Sendo assim é necessário a utilização do .models vistoque o models é o nome do módulo e o
#   "." (ponto) é a estrutura do pacote (pakage)
from .models import Medico, Especialidade, Consulta, Procedimento

# O registro é feito através do modulo contrib, previamente importado pelo DJango
# Para acontecer o registro é necessário dentro do atributo "site" executar o método
#   "register" passando por parâmetro o modelo, para este caso Medico
admin.site.register(Medico)
admin.site.register(Especialidade)
admin.site.register(Consulta)
admin.site.register(Procedimento)