from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from Controllers.user_cadastro_controller import UserCadastroController
from utils.conf_db import conf_db

db = conf_db()
user_cadastro_blueprint = Blueprint('register', __name__)
user_cadastro_controller = UserCadastroController(db)

@user_cadastro_blueprint.route('/register', methods=['POST'])
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

#@user_blueprint.route('/update-user/<user_id>', methods=['PUT']), apos isso nao precisa mais passar o id na requisicao
@user_cadastro_blueprint.route('/update-user', methods=['PUT'])
@jwt_required()
def update_user_route():
    current_user_email = get_jwt_identity()
    update_data = request.json
    #response, status = user_cadastro_controller.update_user(current_user_email, user_id, update_data)
    response, status = user_cadastro_controller.update_user(current_user_email, update_data)
    return jsonify(response), status


##rota do get user data do cadastro_user
@user_cadastro_blueprint.route('/get-user/<user_id>', methods=['GET'])
@jwt_required()
def get_user_data_route(user_id):
    response, status = user_cadastro_controller.get_user_data(user_id)
    return jsonify(response), status

@user_cadastro_blueprint.route('/delete-user/<user_id>', methods=['DELETE'] )
@jwt_required()
def delete_user_route(user_id):
    current_user_email = get_jwt_identity()
    #user_id = get_jwt_identity()##adicionado as 10:50 do dia 29/07 como teste de hipotese, testar ainda
    response, status = user_cadastro_controller.delete_user(current_user_email, user_id)
    return jsonify(response), status
