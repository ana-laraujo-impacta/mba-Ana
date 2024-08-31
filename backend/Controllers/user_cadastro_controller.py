##get, id_login, post, put(para alteracao de cadastro)
##get[cadastro /id do login]
##post [cadastro/]
##put [cadastro/id]
## lucas
from flask_bcrypt import Bcrypt
import unicodedata
from bson import ObjectId
from flask_jwt_extended import jwt_required, get_jwt_identity
import pymongo

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
    def update_user(self, current_user_email,  update_data): ##tirei o user_id desse parametro agora ele valida via email,ja e automatico nao precisa passar o email na requisicao
        
        #user = self.cad_usuario.find_one({'_id': ObjectId(user_id)})
        user = self.cad_usuario.find_one({'email': current_user_email})
        

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
            #{'_id': ObjectId(user_id)}, aqui valida via id
            {'email': current_user_email}, #aqui autentica via email
            {'$set': update_data}
        )

        if result.matched_count:
            return {'message': 'Dados do usuário atualizados com sucesso!'}, 200
        return {'message': 'Usuário não encontrado!'}, 404
    
    ##implementando o get all user retornando todos os dados do cliente
    def get_all_users(self):
        users = self.cad_usuario.find()
        user_list = []
        for user in users:
            user['_id'] = str(user['_id']) ##converte objeto para string
            user_list.append({
                'nome':user.get('nome'),
                'sob_nome':user.get('sob_nome'),
                'cpf': user.get('cpf'),
                'telefone': user.get('telefone'),
                'email': user.get('email'),
                'rua': user.get('rua'),
                'numero':user.get('numero'),
                'bairro':user.get('bairro'),
                'complemento':user.get('complemento'),
                'cidade': user.get('cidade'),
                'cep': user.get('cep'),
                'tp_cad': user.get('tp_cad')
            })
        return {'users': user_list}, 200
    
    
    
## criar um metodo get para pegar todos os dados cadastrados daquele email/usuario especifico que esta logado
##colocar o @jwt_required() da rota aqui  
    
    def get_user_data(self, user_id):
        try:
            user_id = ObjectId(user_id)
        except Exception as e:
            return {'message': 'Id de usuario inválido!'}, 400
        
        user = self.cad_usuario.find_one({'_id': user_id})
        
        if not user:
            return {'message': 'Usuario nao encontrado'}, 404
    
        #converter o id de volta para string para retorna a resposta
        user['_id'] = str(user['_id'])
        
        user_data = {
            'nome': user.get('nome'),
            'sob_nome':user.get('sob_nome'),
            'cpf': user.get('cpf'),
            'telefone': user.get('telefone'),
            'email': user.get('email'),
            'rua': user.get('rua'),
            'numero':user.get('numero'),
            'bairro': user.get('bairro'),
            'complemento': user.get('complemento'),
            'cidade': user.get('cidade'),
            'cep': user.get('cep'),
            'tp_cad': user.get('tp_cad')
        }
        
        return {'user_data': user_data}, 200
    
    @jwt_required()
    def delete_user(self, current_user_email, user_id):                           ##delete pronto
        user = self.cad_usuario.find_one({'_id': ObjectId(user_id)})
        
        if not user:
            return {'message': 'usuario nao encontrado !'}, 404
        
        elif user['email'] != current_user_email:
            return {'message': 'voce nao tem permissao para deletar esse usuario!'}, 403
        
        result = self.cad_usuario.delete_one({'_id': ObjectId(user_id)})
        
        if result.deleted_count:
            return {'message': 'usuario deletado com sucesso'}, 200
        return {'message': 'Erro ao deletar usuario'}, 500
    