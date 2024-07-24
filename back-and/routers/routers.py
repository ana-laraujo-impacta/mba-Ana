##todas as rotas aqui
import os
from flask import Blueprint, request, jsonify
from Controllers.login import AuthController
from Controllers.perguntas_frequentes import FaqController
from Controllers.pesquisa import UserController
from Controllers.cadastro_user import UserCadastroController
from pymongo import MongoClient
from dotenv import load_dotenv
import certifi

load_dotenv()


auth_blueprint = Blueprint('auth', __name__)
user_blueprint = Blueprint('user', __name__)

mongodb_uri = os.getenv("MONGODB_URL")
client = MongoClient(mongodb_uri, tlsCAFile=certifi.where())
database_name = os.getenv("DATABASE_NAME")
db = client[database_name]

auth_controller = AuthController(db)
faq_controller = FaqController(db)
user_controller = UserController(db)
user_cadastro_controller = UserCadastroController(db)

@auth_blueprint.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    response, status = auth_controller.login(email, password)
    return jsonify(response), status

@auth_blueprint.route('/change-password', methods=['POST'])
def change_password():
    data = request.json
    email = data.get('email')
    current_password = data.get('current_password')
    new_password = data.get('new_password')
    response, status = auth_controller.change_password(email, current_password, new_password)
    return jsonify(response), status

@auth_blueprint.route('/faq', methods=['GET'])
def get_all_faqs():
    response, status = faq_controller.get_all_faqs()
    return response, status

@auth_blueprint.route('/faq', methods=['POST'])
def add_faq():
    data = request.json
    pergunta = data.get('pergunta')
    resposta = data.get('resposta')
    response, status = faq_controller.add_faq(pergunta, resposta)
    return response, status

@user_blueprint.route('/search-users', methods=['GET'])
def search_users():
    cidade = request.args.get('cidade', '').strip()
    bairro = request.args.get('bairro', '').strip()
    print(f"Recebido na URL - Cidade: {cidade}, Bairro: {bairro}")  # Debugging
    
    if cidade and bairro:
        response, status = user_controller.search_users_by_location(cidade=cidade, bairro=bairro)
    elif cidade:
        response, status = user_controller.search_users_by_location(cidade=cidade)
    elif bairro:
        response, status = user_controller.search_users_by_location(bairro=bairro)
    else:
        response, status = user_controller.search_users_by_location()

    # response, status = user_controller.search_users_by_location(cidade=cidade, bairro=bairro)
    return response, status

@user_blueprint.route('/users', methods=['GET'])
def get_all_users():
    response, status = user_controller.get_all_users()
    return response, status

@user_blueprint.route('/register', methods=['POST'])
def register():
    data = request.json
    required_fields = ['nome', 'sob_nome', 'cpf', 'telefone', 'email', 'senha', 'rua', 'numero', 'bairro', 'complemento', 'cidade', 'cep', 'tp_cad']
    
    # Verificar se todos os campos obrigatórios estão presentes
    if not all(field in data for field in required_fields):
        return jsonify({'message': 'Faltam campos obrigatórios!'}), 400
    
    nome = data['nome']
    sob_nome = data['sob_nome']
    cpf = data['cpf']
    telefone = data['telefone']
    email = data['email']
    senha = data['senha']
    rua = data['rua']
    numero = data['numero']
    bairro = data['bairro']
    complemento = data['complemento']
    cidade = data['cidade']
    cep = data['cep']
    tp_cad = data['tp_cad']

    response, status = user_cadastro_controller.register(nome, sob_nome, cpf, telefone, email, senha, rua, numero, bairro, complemento, cidade, cep, tp_cad)
    return jsonify(response), status
