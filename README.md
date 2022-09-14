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
NOTE: Projeto é o local que o motor do DJango é executado, com isso as configurações são feitas dentro dele, utilizando o arquivo settings.py

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
NOTE: o APP (aplicação) será o local no DJango que será implementado toda a lógica. Lembrando que um projeto pode ser vários APPs.

```
python -m manage startapp consultas
```

