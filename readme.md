# Gerenciador de Gastos - API

## Descrição
API para gerenciamento de gastos, permitindo que o usuário:
- Cadastre-se na plataforma
- Cadastre e gerencie suas contas
- Cadastre e gerencie as transações de uma conta

## Tecnologias Utilizadas
- Python 3.8
- Docker
- Docker Compose
- MySQL

## Como Rodar o Projeto
### Utilizando Virtualenv
1. Crie e ative um ambiente virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # No Windows, use venv\Scripts\activate
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute o projeto:
   ```bash
   python app.py
   ```

### Utilizando Docker
1. Execute o comando abaixo para subir o ambiente:
   ```bash
   docker-compose up -d --build
   ```

## Acesso ao Projeto
- O projeto roda localmente na porta **8000**
  ```
  http://localhost:8000
  ```