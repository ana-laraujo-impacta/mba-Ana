# API Documentation

## Fazer Login

**Endpoint:** `POST /login`


POST http://localhost:7000/login

{
  "Email": "ana@email.com",
  "Senha": "789456"
}

**Endpoint:** `Alteração de Senha`
Endpoint: POST /change-password


POST http://localhost:7000/change-password

{
  "email": "ana.santos101110@example.com",
  "current_password": "senha123",
  "new_password": "senha1234"
}

**Endpoint:** `FAQ`
Obter FAQ
Endpoint: GET /faq

GET http://localhost:7000/faq

**Endpoint:** `Adicionar FAQ`
Endpoint: POST /faq

POST http://localhost:7000/faq

{
    "pergunta": "O que devo informar para Pet Sitting?",
    "resposta": "É importante fornecer as seguintes informações para o Pet Sitting: Saúde do Pet: Detalhes sobre a saúde geral do seu pet. Medicação: Se o pet toma alguma medicação, especifique quais e em que horários. Vacinações: Confirme se as vacinações do seu pet estão em dia. Comportamento: Informações sobre o comportamento do seu pet, incluindo hábitos, temperamento e qualquer comportamento especial a ser observado. Essas informações ajudam a garantir que seu pet receba o melhor cuidado possível!"
}

**Endpoint:** `Pesquisa`
Buscar Usuários por Cidade e Bairro
Endpoint: GET /search-users?cidade={cidade}&bairro={bairro}
GET http://localhost:7000/search-users?cidade=Sao%20Paulo&bairro=Centro

Buscar Usuários por Bairro
Endpoint: GET /search-users?bairro={bairro}
GET http://localhost:7000/search-users?bairro=Centro

Buscar Usuários por Cidade
Endpoint: GET /search-users?cidade={cidade}
GET http://localhost:7000/search-users?cidade=Sao%20Paulo

**Endpoint:** `Buscar Usuários Cadastrados`
Endpoint: GET /users
GET http://localhost:7000/users

**Endpoint:** `Cadastro de Usuário`
Endpoint: POST /register
POST http://localhost:7000/register

{
    "nome": "Ana",
    "sob_nome": "Santos",
    "cpf": "12345678900",
    "telefone": "123456789",
    "email": "ana.santos101110@example.com",
    "senha": "senha123",
    "rua": "Rua A",
    "numero": "123",
    "bairro": "Centro",
    "complemento": "Apto 1",
    "cidade": "São Paulo",
    "cep": "01000-000",
    "tp_cad": 2
}