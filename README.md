# Controle de Manutenção de Equipamentos

## Objetivo do Projeto

O projeto foi proposto pelo professor Carlos Anderson, do Instituto Federal Baiano – _Campus_ Guanambi, como requisito da disciplina de Laboratório de Programação Web I, integrante do curso de Análise e Desenvolvimento de Sistemas.

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

3. **Execute as migrações**:
   ```sh
   python manage.py migrate
   ```

4. **Crie um superusuário ( para acessar o admin)**:
   ```sh
   python manage.py createsuperuser
   ```

5. **Inicie o servidor de desenvolvimento**:
   ```sh
   python manage.py runserver
   ```

6. **Acesse o sistema**:
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

## Link do vídeo 

LINK:[Trabalho Final WEB I](https://youtu.be/K3mj4tiFAeQ)
