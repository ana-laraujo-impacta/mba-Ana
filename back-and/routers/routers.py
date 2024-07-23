##todas as rotas aqui
import os
from flask import Blueprint, request, jsonify
from Controllers.login import AuthController
from Controllers.perguntas_frequentes import FaqController
from Controllers.pesquisa import UserController
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
    latitude = float(request.args.get('latitude'))
    longitude = float(request.args.get('longitude'))
    cidade = request.args.get('cidade')
    bairro = request.args.get('bairro')
    response, status = user_controller.search_users_by_location(latitude, longitude, cidade, bairro)
    return response, status

