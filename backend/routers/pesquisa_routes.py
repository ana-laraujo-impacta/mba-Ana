from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from Controllers.pesquisa_controller import UserController
from Controllers.user_cadastro_controller import UserCadastroController
from utils.conf_db import conf_db

db = conf_db()
search_blueprint = Blueprint('search', __name__)
user_controller = UserController(db)
user_cadastro_controller = UserCadastroController(db)


@search_blueprint.route('/search-users', methods=['GET'])
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


@search_blueprint.route('/users', methods=['GET'])
def get_all_users():
    response, status = user_cadastro_controller.get_all_users()
    return response, status