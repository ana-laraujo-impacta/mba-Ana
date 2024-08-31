from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from Controllers.faq_controller import FaqController
from utils.conf_db import conf_db

db = conf_db()
faq_blueprint = Blueprint('faq', __name__)
faq_controller = FaqController(db)


@faq_blueprint.route('/faq', methods=['GET'])
def get_all_faqs():
    response, status = faq_controller.get_all_faqs()
    return response, status

@faq_blueprint.route('/faq', methods=['POST'])
def add_faq():
    data = request.json
    pergunta = data.get('pergunta')
    resposta = data.get('resposta')
    response, status = faq_controller.add_faq(pergunta, resposta)
    return response, status