##todas as rotas aqui
from flask import Blueprint, request, jsonify
from Controllers.login_sitter import AuthController

auth_blueprint = Blueprint('auth', __name__)
auth_controller = AuthController()

@auth_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('Email')
    password = data.get('Senha')
    response, status = auth_controller.login(email, password)
    return jsonify(response), status

@auth_blueprint.route('/change-password', methods=['POST'])
def change_password():
    data = request.get_json()
    email = data.get('Email')
    current_password = data.get('SenhaAtual')
    new_password = data.get('NovaSenha')
    response, status = auth_controller.change_password(email, current_password, new_password)
    return jsonify(response), status
