##post [endpoint:/login], get[/], logout?
#ana

from flask_bcrypt import Bcrypt
import json

class AuthController:

    def __init__(self):
        self.json_file = 'mba-Ana/back-and/models/cadastro_petsitter.json'
        self.bcrypt = Bcrypt()

    def load_users(self):
        with open(self.json_file, 'r') as file:
            return json.load(file)

    def save_users(self, users):
        with open(self.json_file, 'w') as file:
            json.dump(users, file, indent=4)

    def login(self, email, password):
        users = self.load_users()
        user = next((u for u in users if u['Email'] == email), None)
        if user and self.bcrypt.check_password_hash(user['Senha'], password):
            return {'message': 'Login bem-sucedido!'}, 200
        return {'message': 'Credenciais inválidas!'}, 401

    def change_password(self, email, current_password, new_password):
        users = self.load_users()
        user = next((u for u in users if u['Email'] == email), None)
        if user and self.bcrypt.check_password_hash(user['Senha'], current_password):
            user['Senha'] = self.bcrypt.generate_password_hash(new_password).decode('utf-8')
            self.save_users(users)
            return {'message': 'Senha alterada com sucesso!'}, 200
        return {'message': 'Credenciais inválidas!'}, 401
