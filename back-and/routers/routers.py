##todas as rotas aqui
import os
from flask import Blueprint, request, jsonify
from Controllers.login import AuthController
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()


auth_blueprint = Blueprint('auth', __name__)

mongodb_uri = os.getenv("MONGODB_URL")
client = MongoClient(mongodb_uri)
database_name = os.getenv("DATABASE_NAME")
db = client[database_name]

auth_controller = AuthController(db)

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
