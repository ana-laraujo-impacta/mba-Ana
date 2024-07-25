##get, id_login, post, put(para alteracao de cadastro)
##get[cadastro /id do login]
##post [cadastro/]
##put [cadastro/id]
## lucas

from flask_bcrypt import Bcrypt
import unicodedata
from bson import ObjectId
from flask_jwt_extended import jwt_required

def normalize_string(s):
    return unicodedata.normalize('NFKD', s).encode('ASCII', 'ignore').decode('ASCII').lower()

class UserCadastroController:
    
    def __init__(self, db):
        self.db = db 
        self.bcrypt = Bcrypt()
        self.cad_usuario = self.db['cad_usuario']
        
    def register(self, nome, sob_nome, cpf, telefone, email, senha, rua, numero, bairro, complemento, cidade, cep, tp_cad):
        if self.cad_usuario.find_one({'email': email}):
            return {'message': 'Email já cadastrado!'}, 409  # Alterado para código de conflito
        
        hashed_password = self.bcrypt.generate_password_hash(senha).decode('utf-8')
        user_data = {
            'nome': nome,
            'sob_nome': sob_nome,
            'cpf': cpf,
            'telefone': telefone,
            'email': email,
            'senha': hashed_password,
            'rua': rua,
            'numero': numero,
            'bairro': normalize_string(bairro),
            'complemento': complemento,
            'cidade': normalize_string(cidade),
            'cep': cep,
            'tp_cad': tp_cad,  # Definido de acordo com a escolha do usuário
        }
        
        result = self.cad_usuario.insert_one(user_data)
        return {'message': 'Cadastro bem-sucedido!', 'id': str(result.inserted_id)}, 201
    
    
    @jwt_required()
    def update_user(self, current_user_email, user_id, update_data):
        
        user = self.cad_usuario.find_one({'_id': ObjectId(user_id)})

        if not user:
            return {'message': 'Usuário não encontrado!'}, 404

        if user['email'] != current_user_email:
            return {'message': 'Você não tem permissão para atualizar este usuário!'}, 403

        if 'senha' in update_data:
            update_data['senha'] = self.bcrypt.generate_password_hash(update_data['senha']).decode('utf-8')

        if 'bairro' in update_data:
            update_data['bairro'] = normalize_string(update_data['bairro'])

        if 'cidade' in update_data:
            update_data['cidade'] = normalize_string(update_data['cidade'])

        result = self.cad_usuario.update_one(
            {'_id': ObjectId(user_id)},
            {'$set': update_data}
        )

        if result.matched_count:
            return {'message': 'Dados do usuário atualizados com sucesso!'}, 200
        return {'message': 'Usuário não encontrado!'}, 404