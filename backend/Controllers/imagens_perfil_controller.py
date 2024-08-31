import boto3
import os
from botocore.exceptions import NoCredentialsError
from bson import ObjectId
from flask_jwt_extended import jwt_required
from utils.aws_utils import upload_to_s3, delete_from_s3, delete_folder_from_s3


s3_client = boto3.client(
    's3',
    aws_access_key_id= os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key= os.getenv('AWS_SECRET_ACCESS_KEY'),
    region_name= os.getenv('REGION_NAME')
)


def upload_to_s3(file, bucket_name, s3_path):
    try:
        # Remover possíveis aspas duplas ou simples no caminho
        s3_path = s3_path.replace('"', '').replace("'", "")

        # Verificar se há barras adicionais ou ausentes e ajustar
        s3_client.upload_fileobj(file, bucket_name, s3_path)
        
        # Garantir que a URL esteja corretamente formatada
        url = f"https://{bucket_name}.s3.amazonaws.com/{s3_path}"
        return url
    except NoCredentialsError:
        return None

class ImagensPerfilController:
    def __init__(self, db):
        self.db = db
        self.imagens_perfil = self.db['imagens_perfil']

    @jwt_required()
    def create_imagens_perfil(self, cpf, email, foto_perfil_url, fotos_pets_urls):
        imagens_data = {
            'cpf': cpf,
            'email': email,
            'foto_perfil': foto_perfil_url,
            'fotos_pets': fotos_pets_urls
        }
        # self.db.create_collection('imagens_perfil')
        result = self.imagens_perfil.insert_one(imagens_data)
        imagens_perfil = self.imagens_perfil.find_one({'cpf': cpf})
        print(imagens_perfil)
        return {'message': 'Imagens de perfil salvas com sucesso!', 'id': str(result.inserted_id)}, 201

    # @jwt_required()
    # def get_imagens_perfil(self, cpf):
    #     imagens_perfil = self.imagens_perfil.find_one({'cpf': cpf})
    #     print(imagens_perfil)
    #     if not imagens_perfil:
    #         return {'message': 'Cadastro complementar não encontrado!'}, 404

    #     imagens_perfil['cpf'] = str(imagens_perfil['cpf'])
    #     return {'imagens_perfil_data': imagens_perfil}, 200
    @jwt_required()
    def get_imagens_perfil(self, cpf):
        imagens_perfil = self.imagens_perfil.find_one({'cpf': cpf})
        if not imagens_perfil:
            return {'message': 'Cadastro complementar não encontrado!'}, 404
        
        if '_id' in imagens_perfil:
            imagens_perfil['_id'] = str(imagens_perfil['_id'])

        return {'imagens_perfil_data': imagens_perfil}, 200

    @jwt_required()
    def update_imagens_perfil(self, cpf, foto_perfil=None, fotos_pets=None):
        imagens_perfil = self.imagens_perfil.find_one({'cpf': cpf})
        if not imagens_perfil:
            return {'message': 'Cadastro complementar não encontrado!'}, 404
        
        update_fields = {}

        if foto_perfil:
            perfil_path = f"{cpf}/perfil/{foto_perfil.filename}"
            foto_url = upload_to_s3(foto_perfil, 'bucket-s3-pets', perfil_path)
            delete_from_s3('bucket-s3-pets', imagens_perfil['foto_perfil'].split('.com/')[1])
            update_fields['foto_perfil'] = foto_url

        if fotos_pets:
            fotos_urls = []
            for foto in fotos_pets:
                pet_path = f"{cpf}/{foto.filename}"
                foto_pet_url = upload_to_s3(foto, 'bucket-s3-pets', pet_path)
                delete_from_s3('bucket-s3-pets', foto_pet_url.split('.com/')[1])
                fotos_urls.append(foto_pet_url)
            update_fields['fotos_pets'] = fotos_urls

        if update_fields:
            self.imagens_perfil.update_one({'cpf': cpf}, {'$set': update_fields})
            return {'message': 'Imagens atualizadas com sucesso!'}, 200
        else:
            return {'message': 'Nada para atualizar.'}, 400

    @jwt_required()
    def delete_imagens_perfil(self, cpf, tipo_imagem=None, imagem_url=None):
        imagens_perfil = self.imagens_perfil.find_one({'cpf': cpf})
        if not imagens_perfil:
            return {'message': 'Cadastro complementar não encontrado!'}, 404

        if tipo_imagem == 'perfil' and imagens_perfil['foto_perfil'] == imagem_url:
            delete_from_s3('bucket-s3-pets', imagem_url.split('.com/')[1])
            self.imagens_perfil.update_one({'cpf': cpf}, {'$unset': {'foto_perfil': ""}})
            return {'message': 'Imagem de perfil deletada com sucesso!'}, 200
        elif tipo_imagem == 'pet' and imagem_url in imagens_perfil['fotos_pets']:
            delete_from_s3('bucket-s3-pets', imagem_url.split('.com/')[1])
            self.imagens_perfil.update_one({'cpf': cpf}, {'$pull': {'fotos_pets': imagem_url}})
            return {'message': 'Imagem de pet deletada com sucesso!'}, 200
        else:
            return {'message': 'Imagem não encontrada.'}, 404

    @jwt_required()
    def delete_perfil(self, cpf):
        # Verifica se o perfil existe no banco de dados
        imagens_perfil = self.imagens_perfil.find_one({'cpf': cpf})
        if not imagens_perfil:
            return {'message': 'Perfil não encontrado!'}, 404

        # Deletar a pasta do usuário no bucket S3
        delete_folder_from_s3('bucket-s3-pets', f"{cpf}/")

        # Deletar o registro no banco de dados
        result = self.imagens_perfil.delete_one({'cpf': cpf})
        print(f"Deleted count: {result.deleted_count}")
        if result.deleted_count > 0:
            return {'message': 'Cadastro complementar deletado com sucesso!'}, 200
        return {'message': 'Falha ao deletar o cadastro complementar!'}, 400
