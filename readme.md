**# API Documentation**

**## Fazer Login**

_***Endpoint:***_  `POST /login`

POST [http://localhost:7000/login](http://localhost:7000/login)

```json

{

"email": "[ana.santos23@example.com](mailto:ana.santos23@example.com)",

"senha": "senha123"

}

```

_***Endpoint:***_  `Alteração de Senha`

Endpoint: POST /change-password

POST [http://localhost:7000/change-password](http://localhost:7000/change-password)

```json

{

"email": "[ana.santos23@example.com](mailto:ana.santos23@example.com)",

"current_password": "senha123",

"new_password": "senha1234"

}

```

_***Endpoint:***_  `FAQ`

Obter FAQ

Endpoint: GET /faq

GET [http://localhost:7000/faq](http://localhost:7000/faq)

_***Endpoint:***_  `Adicionar FAQ`

Endpoint: POST /faq

POST [http://localhost:7000/faq](http://localhost:7000/faq)

```json

{

"pergunta": "O que devo informar para Pet Sitting?",

"resposta": "É importante fornecer as seguintes informações para o Pet Sitting: Saúde do Pet: Detalhes sobre a saúde geral do seu pet. Medicação: Se o pet toma alguma medicação, especifique quais e em que horários. Vacinações: Confirme se as vacinações do seu pet estão em dia. Comportamento: Informações sobre o comportamento do seu pet, incluindo hábitos, temperamento e qualquer comportamento especial a ser observado. Essas informações ajudam a garantir que seu pet receba o melhor cuidado possível!"

}

```

_***Endpoint:***_  `Pesquisa`

Buscar Usuários por Cidade e Bairro

Endpoint: GET /search-users?cidade={cidade}&bairro={bairro}

GET [http://localhost:7000/search-users?cidade=Sao%20Paulo&bairro=Centro](http://localhost:7000/search-users?cidade=Sao%20Paulo&bairro=Centro)

Buscar Usuários por Bairro

Endpoint: GET /search-users?bairro={bairro}

GET [http://localhost:7000/search-users?bairro=Centro](http://localhost:7000/search-users?bairro=Centro)

Buscar Usuários por Cidade

Endpoint: GET /search-users?cidade={cidade}

GET [http://localhost:7000/search-users?cidade=Sao%20Paulo](http://localhost:7000/search-users?cidade=Sao%20Paulo)

_***Endpoint:***_  `Buscar Usuários Cadastrados`

Endpoint: GET /users

GET [http://localhost:7000/users](http://localhost:7000/users)

_***Endpoint:***_  `Cadastro de Usuário`

Endpoint: POST /register

POST [http://localhost:7000/register](http://localhost:7000/register)

```json

{

"nome": "Ana",

"sob_nome": "Santos",

"cpf": "12345678900",

"telefone": "123456789",

"email": "[ana.santos101110@example.com](mailto:ana.santos101110@example.com)",

"senha": "senha123",

"rua": "Rua A",

"numero": "123",

"bairro": "Centro",

"complemento": "Apto 1",

"cidade": "São Paulo",

"cep": "01000-000",

"tp_cad": 2

}

```

_***Endpoint:***_  `Alterar Cadastro de Usuário`

Endpoint: [http://localhost:7000/update-user/](http://localhost:7000/update-user/)<_id>

PUT : É possivel alterar qualquer dado do usuario.

```json

{

"nome": "Anateste3"

}

```

**Configuração de autenticação por token**

O token é gerado automaticamente toda vez que é feito o login, deve ser usado nas requisições:

update_user, search_users e change_password

**Extensão usada Flask-JWT-Extended**

É uma extensão que facilita a adição de autenticação baseada em JWT (JSON Web Tokens)

**Como usar no postman** :

1 - Efetuar o login do usuario pelo endpoint Login;

2 - Copiar o token do response;

3 - Exemplo no endpoint **update_user**:

colocar a url [http://localhost:7000/update-user/66a1a6294997d80e708fe3dd](http://localhost:7000/update-user/66a1a6294997d80e708fe3dd) , metodo PUT;

Clicar em Authorization que esta na guia abaixo do campo da url, dentro de Authorization em AuthType selecionar Bearer Token , no campo Token colar o token sem aspas