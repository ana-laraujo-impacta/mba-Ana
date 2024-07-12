from flask import Flask
from flask_bcrypt import Bcrypt
import json

app = Flask(__name__)
bcrypt = Bcrypt(app)

users = [
    {
        "nome": "Ana",
        "sobrenome": "Lima",
        "cpf": "01102203345",
        "telefone": "11 992208331",
        "Cidade": "Sao paulo",
        "Bairro": "jardins",
        "Endereco": "Rua e numero",
        "Email": "ana@email.com",
        "Senha": bcrypt.generate_password_hash("789456").decode('utf-8')
    },
    {
        "nome": "Lucas",
        "sobrenome": "Oliveira",
        "cpf": "01102203345",
        "telefone": "68 992208331",
        "Cidade": "Sao paulo",
        "Bairro": "jardins",
        "Endereco": "Rua e numero",
        "Email": "lucas@email.com",
        "Senha": bcrypt.generate_password_hash("123456").decode('utf-8')
    }
]

with open('cadastro_user.json', 'w') as file:
    json.dump(users, file, indent=4)

print("Senhas hashadas e salvas com sucesso!")
