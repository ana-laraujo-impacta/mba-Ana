##post [endpoint:/login], get[/], logout?
#ana
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token
import datetime


class AuthController:

    def __init__(self, db):
        self.db = db
        self.bcrypt = Bcrypt()
        self.users_collection = self.db['cad_usuario']

    # def login(self, email, password):
    #     user = self.users_collection.find_one({"email": email})
    #     if not user:
    #         return {'message': 'Email não cadastrado. Por favor, faça o cadastro.'}, 404
    #     if user and self.bcrypt.check_password_hash(user['senha'], password):
    #         return {'message': 'Login bem-sucedido!'}, 200
    #     return {'message': 'Credenciais inválidas!'}, 401

    def login(self, email, password):
        user = self.users_collection.find_one({"email": email})
        if not user:
            return {'message': 'Email não cadastrado. Por favor, faça o cadastro.'}, 404
        if user and self.bcrypt.check_password_hash(user['senha'], password):
            access_token = create_access_token(identity=email, expires_delta=datetime.timedelta(hours=1))
            return {'message': 'Login bem-sucedido!', 'access_token': access_token}, 200
        return {'message': 'Credenciais inválidas!'}, 401

    def change_password(self, email, current_password, new_password):
        user = self.users_collection.find_one({"email": email})
        if user and self.bcrypt.check_password_hash(user['senha'], current_password):
            new_hashed_password = self.bcrypt.generate_password_hash(new_password).decode('utf-8')
            self.users_collection.update_one({"email": email}, {"$set": {"senha": new_hashed_password}})
            return {'message': 'Senha alterada com sucesso!'}, 200
        return {'message': 'Credenciais inválidas!'}, 401
    