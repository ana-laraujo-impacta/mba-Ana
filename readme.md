# Meu Projeto Python

Este é o README para o meu projeto Python. Ele explica como configurar e rodar o projeto.

## Dependências

Este projeto requer as seguintes dependências:

- aniso8601==9.0.1
- attrs==23.2.0
- blinker==1.8.2
- click==8.1.7
- colorama==0.4.6
- Flask==3.0.3
- flask-restplus==0.13.0
- flask-restx==1.3.0
- importlib_resources==6.4.0
- itsdangerous==2.2.0
- Jinja2==3.1.4
- jsonschema==4.23.0
- jsonschema-specifications==2023.12.1
- MarkupSafe==2.1.5
- pytz==2024.1
- referencing==0.35.1
- rpds-py==0.19.0
- six==1.16.0
- Werkzeug==3.0.3

## Instalação

1. Clone o repositório para a sua máquina local:

    ```sh
    git clone <URL do repositório>
    cd <nome do repositório>
    ```

2. Crie um ambiente virtual:

    ```sh
    python -m venv venv
    ```

3. Ative o ambiente virtual:

    - No Windows:
    
        ```sh
        venv\Scripts\activate
        ```
    
    - No macOS/Linux:
    
        ```sh
        source venv/bin/activate
        ```

4. Instale as dependências:

    ```sh
    pip install -r requirements.txt
    ```

## Executando o Projeto

Para rodar o projeto, execute o seguinte comando na raiz do repositório:

```sh
python app.py
