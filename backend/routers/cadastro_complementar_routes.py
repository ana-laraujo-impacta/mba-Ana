from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from Controllers.cadastro_complementar_controller import CadastroComplementarController
from utils.conf_db import conf_db

db = conf_db()
cadastro_complementar_blueprint = Blueprint('complementar', __name__)
cadastro_complementar_controller = CadastroComplementarController(db)

@cadastro_complementar_blueprint.route('/complementar', methods=['POST'])
def create_complementar():
    data = request.json
    cpf = data.get('cpf')
    email = data.get('email')
    nome_emergencia = data.get('nome_emergencia')
    tipo_pet = data.get('tipo_pet')
    tipo_cuidado = data.get('tipo_cuidado')
    bio_msg = data.get('bio_msg')
    tb_cap = data.get('tb_cap')

    response, status = cadastro_complementar_controller.create_complementar(cpf, email, nome_emergencia, tipo_pet, tipo_cuidado, bio_msg, tb_cap)
    return jsonify(response), status

@cadastro_complementar_blueprint.route('/complementar/<complementar_id>', methods=['GET'])
@jwt_required()
def get_complementar(complementar_id):
    response, status = cadastro_complementar_controller.get_complementar(complementar_id)
    return jsonify(response), status

@cadastro_complementar_blueprint.route('/complementar/<complementar_id>', methods=['PUT'])
@jwt_required()
def update_complementar(complementar_id):
    user_id = get_jwt_identity()  # Assume que o CPF foi usado como identidade do JWT
    update_data = request.json
    response, status = cadastro_complementar_controller.update_complementar(user_id, complementar_id, update_data)
    return jsonify(response), status

@cadastro_complementar_blueprint.route('/complementar/<complementar_id>', methods=['DELETE'])
@jwt_required()
def delete_complementar(complementar_id):
    response, status = cadastro_complementar_controller.delete_complementar(complementar_id)
    return jsonify(response), status
