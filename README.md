# Cars API

Este é um projeto de API RESTful para gerenciamento de veículos, desenvolvido com Django e Django Rest Framework (DRF). A API oferece operações CRUD (Create, Read, Update, Delete) e utiliza recursos avançados como autenticação JWT, filtros com RQL, e uma interface administrativa customizada com django-jazzmin.

## Índice

- [Funcionalidades](#funcionalidades)
- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Documentação](#documentação-e-informações-adicionais)

## Funcionalidades

- **Autenticação JWT**: Autenticação baseada em tokens JWT.
- **Permissões**: Esquema de permissões de usuários do Django e permissões personalizadas.
- **Filtros RQL**: Filtros avançados utilizando Resource Query Language.
- **Admin Customizado**: Painel administrativo customizado com django-jazzmin.
- **Documentação Automática**: Geração automática de documentação de API com Swagger.
- **Fixtures**: Possibilidade de carregar dados iniciais a partir de arquivos JSON.
- **Operações CRUD**: Operações completas de criação, leitura, atualização e exclusão de veículos.
- **Paginação**: Recurso de paginação do Django Rest Framework.

## Requisitos

Para rodar este projeto, você precisará de:

- **Pipenv** (todos os requisitos necessários estão no arquivo Pipfile)

## Instalação

Siga os passos abaixo para configurar o projeto localmente:

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/jardeson-ferreira/cars_api.git
   cd cars_api

2. **Ative o ambiente virtual**:

   ```bash
   pipenv shell

2. **Faça as migrações do banco de dados e carregue os dados iniciais a partir do arquivo de fixtures**:
   
   ```bash
   python manage.py migrate
   python manage.py loaddata initial_data

3. **Execute o servidor de desenvolvimento**:

   ```bash
   python manage.py runserver

## Documentação e Informações Adicionais

- Acesse a documentação Swagger no navegador em: http://localhost:8000/swagger/ e http://localhost:8000/redoc/
- Admin Customizado: Acesse o painel administrativo customizado em http://localhost:8000/admin (login necessário).
- Filtragem avançada dos dados da API com RQL, consulte como utilizar em: https://django-rql.readthedocs.io/.
- Usuário para login após o carregamento do dados iniciais do arquivo de fixtures:

  ```bash
  username: admin
  password: admin
