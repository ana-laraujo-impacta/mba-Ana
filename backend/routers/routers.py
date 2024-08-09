##todas as rotas aqui
import os
from flask import Blueprint, request, jsonify, Flask
from Controllers.login import AuthController
from Controllers.perguntas_frequentes import FaqController
from Controllers.pesquisa import UserController
from Controllers.cadastro_user import UserCadastroController
from flask_jwt_extended import jwt_required, get_jwt_identity
from pymongo import MongoClient
from dotenv import load_dotenv
import certifi
from flask_cors import cross_origin
from Controllers.cadastro_complementar import CadastroComplementarController


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
cad_complementar_controller = CadastroComplementarController(db)

@auth_blueprint.route('/login', methods=['POST'])
@cross_origin()
def login():
    data = request.json
    email = data.get('email')
    password = data.get('senha')
    response, status = auth_controller.login(email, password)
    return jsonify(response), status

@auth_blueprint.route('/change-password', methods=['POST'])
@jwt_required()
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
@jwt_required()
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

@user_blueprint.route('/update-user/<user_id>', methods=['PUT'])
@jwt_required()
def update_user(user_id):
    current_user_email = get_jwt_identity()
    update_data = request.json
    response, status = user_cadastro_controller.update_user(current_user_email, user_id, update_data)
    return jsonify(response), status


##rota do get user data do cadastro_user
@user_blueprint.route('/get-user/<user_id>', methods=['GET'])
@jwt_required()
def get_user_data_route(user_id):
    response, status = user_cadastro_controller.get_user_data(user_id)
    return jsonify(response), status

@user_blueprint.route('/delete-user/<user_id>', methods=['DELETE'] )
@jwt_required()
def delete_user_route(user_id):
    current_user_email = get_jwt_identity()
    #user_id = get_jwt_identity()##adicionado as 10:50 do dia 29/07 como teste de hipotese, testar ainda
    response, status = user_cadastro_controller.delete_user(current_user_email, user_id)
    return jsonify(response), status


@user_blueprint.route('/complementar', methods=['POST'])
@jwt_required()
def create_complementar():
    data = request.json
    cpf = data.get('cpf')
    email = data.get('email')
    nome_emergencia = data.get('nome_emergencia')
    foto = data.get('foto')
    tipo_pet = data.get('tipo_pet')
    tipo_cuidado = data.get('tipo_cuidado')
    bio_msg = data.get('bio_msg')
    tb_cap = data.get('tb_cap')

    response, status = cad_complementar_controller.create_complementar(cpf, email, nome_emergencia, foto, tipo_pet, tipo_cuidado, bio_msg, tb_cap)
    return jsonify(response), status

@user_blueprint.route('/complementar/<complementar_id>', methods=['GET'])
@jwt_required()
def get_complementar(complementar_id):
    response, status = cad_complementar_controller.get_complementar(complementar_id)
    return jsonify(response), status

@user_blueprint.route('/complementar/<complementar_id>', methods=['PUT'])
@jwt_required()
def update_complementar(complementar_id):
    user_id = get_jwt_identity()  # Assume que o CPF foi usado como identidade do JWT
    update_data = request.json
    response, status = cad_complementar_controller.update_complementar(user_id, complementar_id, update_data)
    return jsonify(response), status

@user_blueprint.route('/complementar/<complementar_id>', methods=['DELETE'])
@jwt_required()
def delete_complementar(complementar_id):
    response, status = cad_complementar_controller.delete_complementar(complementar_id)
    return jsonify(response), status