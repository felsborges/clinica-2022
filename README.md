# Clínica

A prosta deste projeto é construir uma aplicação web para atender uma clínica.

O objetivo é desenvolver as seguintes telas:
- Médicos
- Especialidades
- Procedimentos
- Consultas

## Preparar o ambiente

1. Instalação do venv

```
python -m venv venv
```

2. Ativar o ambiente virtual (venv)

```
.\venv\Scripts\activate
```

3. Instalação do DJango

```
pip install django
```

## Estrutuação do Projeto

1. Criar o projeto
> NOTE: Projeto é o local que o motor do DJango é executado, com isso as configurações são feitas dentro dele, utilizando o arquivo settings.py

```
django-admin startproject clinica .
```

- django-admin: comando de terminal responsável pela administração do DJango
    - startproject: Parâmetro do comando django-admin responsável por estruturar um projeto em django
        É obrigatório informar o nome do projeto (neste caso clinica).
        Como próximo parâmetro é o diretório que será estruturado o projeto, que a sugestão é informar o caminho relatório do diretório local "."

### Iniciar o serviço Web
```
python -m manage runserver
```
- manage: Módulo do DJango responsável por executar ações dentro do projeto
    - runserver: Parâmetro que determina a execução do módulo web disponível dentro do DJango para desenvolvimento

O site estará disponível no endereço http://127.0.0.1:8000/

2. Criar um APP
> NOTE: o APP (aplicação) será o local no DJango que será implementado toda a lógica. Lembrando que um projeto pode ser vários APPs.

```
python -m manage startapp consultas
```

clinica: pasta que contem os arquivos do projeto
consultas: pasta que trata os arquivos da aplicação

## Adicionando o APP ao Projeto

É necessário entrar no arquivo settings.py e localizar a constante INSTALLED_APPS.
A constante INSTALLED_APPS é uma lista que contém todos os APPs associados ao projeto, somente após um APP estar relacionado nesta lista que o DJango pode identificar e utilizar o APP nos demais fins.

> IMPORTANTE:
> Configurar o TIME_ZONE para que a aplicação seja executado com o horário local.
> https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
> Configurar o linguagem da aplicação no LANGUAGE_CODE
> http://www.i18nguy.com/unicode/language-identifiers.html

```
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'

```


## Registrar o APP à aplicação admin

A aplicação admin é uma interface gerada de maneira automática pelo DJango, que utilizo o modelo desenvolvido na aplicação, para criar uma interface básica de gestão, ou seja, uma tela de lista, detalhes, inclusão, atualização e exclusão.

C -> Create (Criar)
R -> Read (Ler)
U -> Update (Atualizar)
D -> Delete (Excluir)

Para registra o aplicação é necessário localizar o arquivo consultas/admin.py e incluir os comandos de registro do modelo

### Cadastrar o super usuário (admin)

Para acessar a tela de admin é necessário que se tenha um usuário devidamente registrado na aplicação.

```
python -m manage createsuperuser
```

- **createsuperuser**: é o comando utilizado para criar o usuário administrativo da aplicação.

## Migration

O migration (migrações) é o ato de capturar o modelo de dados desenvolvido em uma camada de aplicação, e preprar os códigos necessários para criar o banco de dados.

> IMPORTANTE: o migrate não está vincula a nenhum banco de dados específico

```
python -m manage makemigrations consultas
```

- **makemigrations**: é o comando responsável pela preparação do modelo que será implantando no no banco de dados
    - Como parâmetro é necessário informar o nome da aplicação

Após a execução deste comando, a pasta migrations é criada dentro da aplicação (consultas/migrations).

```
python -m manage migrate consultas
```

- **migrate**: é comando responsável por aplicar a estrutura criada pelo makemigration.

## URLconf

A URLconf é termo utilizado para tratar os arquivos urls.py. Este arquivo está presente no projeto e na aplicação.

O comando startapp não criar o arquivo urls.py na aplicação, é necessáiro criar o arquivo.

> IMPORTANTE: o arquivo deve conter obrigatoriamente uma variável chamda urlpatterns
