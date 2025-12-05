# Controle de Manutenção de Equipamentos

## Objetivo do Projeto

O projeto foi proposto pelo professor Carlos Anderson, do Instituto Federal Baiano – _Campus_ Guanambi, como requisito da disciplina de Laboratório de Programação Web II, integrante do curso de Análise e Desenvolvimento de Sistemas.

A proposta consiste no desenvolvimento de um sistema Web utilizando o framework Django. A equipe composta pelos integrantes Álex Silva Costa, Luísa Mel Almeida Martins e Wilton Silva Rodrigues, optou pelo desenvolvimento de um sistema Web de **controle de manutenção de equipamentos** em uma instituição.

O sistema permitirá o cadastro de equipamentos, setores, técnicos, peças, ordens de manutenção e usuários, facilitando o acompanhamento das manutenções realizadas, o vínculo entre equipamentos e setores, além do controle das peças utilizadas em cada processo.

## Como Executar Localmente

1. **Pré-requisitos**:
   - Python 3.10+
   - Django 5.x
   - Banco de dados SQLite (já incluso)

2. **Instalação**:
   - Clone o repositório ou extraia os arquivos.
   - Acesse a pasta do projeto pelo terminal.

3. **Instalação das dependências**:
   - Instale todas as dependências do projeto com:
   ```sh
   pip install -r requirements.txt
   ```

4. **Execute as migrações**:
   ```sh
   python manage.py migrate
   ```

5. **Crie um superusuário ( para acessar o admin)**:
   ```sh
   python manage.py createsuperuser
   ```

6. **Inicie o servidor de desenvolvimento**:
   ```sh
   python manage.py runserver
   ```

7. **Acesse o sistema**:
   - Abra o navegador e acesse: [http://localhost:8000/](http://localhost:8000/)

## Integrantes do Grupo

- Aléx Silva Costa 
- Luísa Mel Almeida Martins
- Wilton Silva Rodrigues

## Instruções de Acesso

- O sistema possui autenticação de usuários.
- Caso não haja usuários cadastrados, utilize o comando `createsuperuser` para criar um usuário administrador.
- Usuários predefinidos podem ser informados pelo administrador do sistema.
- O acesso ao painel administrativo está disponível em [http://localhost:8000/admin/](http://localhost:8000/admin/).


## API RESTful (Django Rest Framework)

O projeto expõe uma API RESTful completa e segura, desenvolvida com Django Rest Framework (DRF) e autenticação JWT.

### Principais Recursos da API

- **Autenticação JWT:**  
  Endpoints protegidos exigem token JWT para acesso.  
  Obtenha o token via `/api/token/` e renove via `/api/token/refresh/`.

- **CRUD Completo:**  
  Operações de cadastro, consulta, edição e exclusão para Equipamentos, Setores, Técnicos, Peças e Ordens de Manutenção.

- **Models Relacionados:**  
  A API permite gerenciar relações entre equipamentos, setores, técnicos, peças e ordens de manutenção.

- **Documentação Interativa:**  
  Acesse a documentação da API via Swagger (`/swagger/`) ou Redoc (`/redoc/`).

### Como Usar a API

1. **Obtenha o token JWT:**  
   Faça uma requisição POST para `/api/token/` enviando `username` e `password`.  
   Exemplo usando `curl`:
   ```
   curl -X POST http://localhost:8000/api/token/ -d "username=seu_usuario&password=sua_senha"
   ```

2. **Acesse rotas protegidas:**  
   Envie o token JWT no header das requisições:
   ```
   Authorization: Bearer <seu_token>
   ```

3. **Renove o token:**  
   Quando o token expirar, use `/api/token/refresh/` com o refresh token para obter um novo.

### Documentação da API

- [Swagger UI](http://localhost:8000/swagger/)
- [Redoc](http://localhost:8000/redoc/)


## Link do vídeo 

LINK:[Trabalho Final WEB II](https://youtu.be/hX5Ev-Yw5oA?si=jidtAhJRKytsO1Iv)

Se precisar de exemplos de requisições ou integração com cliente mobile, consulte a documentação da API ou entre em contato com os desenvolvedores.
