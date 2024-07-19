##post [endpoint:/login], get[/], logout?
#ana
from flask_bcrypt import Bcrypt


class AuthController:

    def __init__(self, db):
        self.db = db
        self.bcrypt = Bcrypt()
        self.users_collection = self.db['cad_usuario']

    def login(self, email, password):
        user = self.users_collection.find_one({"email": email})
        if user and self.bcrypt.check_password_hash(user['senha'], password):
            return {'message': 'Login bem-sucedido!'}, 200
        return {'message': 'Credenciais inválidas!'}, 401

    def change_password(self, email, current_password, new_password):
        user = self.users_collection.find_one({"email": email})
        if user and self.bcrypt.check_password_hash(user['senha'], current_password):
            new_hashed_password = self.bcrypt.generate_password_hash(new_password).decode('utf-8')
            self.users_collection.update_one({"email": email}, {"$set": {"senha": new_hashed_password}})
            return {'message': 'Senha alterada com sucesso!'}, 200
        return {'message': 'Credenciais inválidas!'}, 401