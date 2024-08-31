from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from Controllers.auth_controller import AuthController
from utils.conf_db import conf_db

db = conf_db()
auth_blueprint = Blueprint('auth', __name__)
auth_controller = AuthController(db)

@auth_blueprint.route('/login', methods=['POST'])
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
