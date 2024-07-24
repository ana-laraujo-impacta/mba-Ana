##get, id_login, post, put(para alteracao de cadastro)
##get[cadastro /id do login]
##post [cadastro/]
##put [cadastro/id]
## lucas

from flask_bcrypt import Bcrypt
import unicodedata

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