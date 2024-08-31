from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from utils.aws_utils import upload_to_s3
from Controllers.imagens_perfil_controller import ImagensPerfilController
from utils.conf_db import conf_db

db = conf_db()
imagens_perfil_blueprint = Blueprint('imagens', __name__)
imagens_perfil_controller = ImagensPerfilController(db)

@imagens_perfil_blueprint.route('/imagens_perfil', methods=['POST'])
@jwt_required()
def imagens_perfil():
    data = request.form
    cpf = data.get('cpf')
    email = data.get('email')

    foto_perfil = request.files.get('foto_perfil')
    fotos_pets = request.files.getlist('fotos_pets')
    
    if not foto_perfil or not fotos_pets:
        return {'message': 'Faltando imagem de perfil ou fotos de pets!'}, 400

    perfil_path = f"{cpf}/perfil/{foto_perfil.filename}"
    foto_url = upload_to_s3(foto_perfil, 'bucket-s3-pets', perfil_path)

    fotos_urls = []
    for i, foto in enumerate(fotos_pets):
        pet_path = f"{cpf}/{foto.filename}"
        foto_pet_url = upload_to_s3(foto, 'bucket-s3-pets', pet_path)
        fotos_urls.append(foto_pet_url)

    print(foto_pet_url)
    print(fotos_urls)

    response, status = imagens_perfil_controller.create_imagens_perfil(cpf, email, foto_url, fotos_urls)

    return jsonify(response), status

@imagens_perfil_blueprint.route('/imagens_perfil/<cpf>', methods=['GET'])
@jwt_required()
def get_imagens_perfil(cpf):
    response, status = imagens_perfil_controller.get_imagens_perfil(cpf)
    return jsonify(response), status

@imagens_perfil_blueprint.route('/imagens_perfil/<cpf>', methods=['PUT'])
@jwt_required()
def update_imagens_perfil(cpf):
    data = request.form
    foto_perfil = request.files.get('foto_perfil')
    fotos_pets = request.files.getlist('fotos_pets')
    
    response, status = imagens_perfil_controller.update_imagens_perfil(cpf, foto_perfil, fotos_pets)
    return jsonify(response), status

@imagens_perfil_blueprint.route('/imagens_perfil/<cpf>', methods=['DELETE'])
@jwt_required()
def delete_imagens_perfil(cpf):
    data = request.json
    tipo_imagem = data.get('tipo_imagem')
    imagem_url = data.get('imagem_url')
    
    response, status = imagens_perfil_controller.delete_imagens_perfil(cpf, tipo_imagem, imagem_url)
    return jsonify(response), status

@imagens_perfil_blueprint.route('/delete_perfil/<cpf>', methods=['DELETE'])
@jwt_required()
def delete_perfil(cpf):
    response, status = imagens_perfil_controller.delete_perfil(cpf)
    return jsonify(response), status
