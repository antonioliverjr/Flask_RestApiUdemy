![](https://www.python.org/static/img/python-logo.png)
# Desenvolvimento com Python

**Aprimorando o conceito Clean, utilizando sintaxe Python**

## Praticando API! Python com princípios da Clean Architeture!

> *Projeto pessoal para utilizar como **Base Python** na criação de:*

- **API**
- **Micro-serviços**

# Anotações do projeto

> Bibliotecas Utilizadas
- Flask (App)
- Flask_Restx (Api e Swagger)
- Inject (IoC e DI)
- SQLAlchemy (Database)
- Alembic (Migrations)
- Python-Decouple (Env)

> Comandos Bash
```bash
alembic revision --autogenerate -m "<nome-da-migration>"
alembic upgrade head
```
> Estrutura de Projeto
- main.py (Instance Server)
- config/settings.py (Configurações)
- controllers (Routers ou Resource) **Utiliza models e services**
- models (DTOs ou ViewModels) **Modelos relativos as entidades, desacopla a dependências destas na parte externa da aplicação**
- services (Bussiness) **Utiliza as Interfaces**
- config/dependency_injection.py (IoC e DI) **Permite as IoC nos Services**
- data (Context, Repositories, Interfaces) **Realiza comunicação com DB e os métodos para os Services**
- entities (Domain) **Entidades do projeto, modelam o DB**


