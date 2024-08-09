from bson import ObjectId
from flask_jwt_extended import jwt_required, get_jwt_identity
from pymongo import MongoClient

class CadastroComplementarController:
    def __init__(self, db):
        self.db = db
        self.cad_complementar = self.db['comp_usuario']

    @jwt_required()
    def create_complementar(self, cpf, email, nome_emergencia, foto, tipo_pet, tipo_cuidado, bio_msg, tb_cap):
        complementar_data = {
            'cpf': cpf,
            'email': email,
            'nome_emergencia': nome_emergencia,
            'foto': foto,  # Caminho da imagem
            'tipo_pet': tipo_pet,
            'tipo_cuidado': tipo_cuidado,
            'bio_msg': bio_msg,
            'tb_cap': tb_cap
        }
        result = self.cad_complementar.insert_one(complementar_data)
        return {'message': 'Cadastro complementar bem-sucedido!', 'id': str(result.inserted_id)}, 201

    @jwt_required()
    def get_complementar(self, complementar_id):
        complementar = self.cad_complementar.find_one({'_id': ObjectId(complementar_id)})
        if not complementar:
            return {'message': 'Cadastro complementar não encontrado!'}, 404

        complementar['_id'] = str(complementar['_id'])
        return {'complementar_data': complementar}, 200

    @jwt_required()
    def update_complementar(self, user_id, complementar_id, update_data):
        complementar = self.cad_complementar.find_one({'_id': ObjectId(complementar_id)})

        if not complementar:
            return {'message': 'Cadastro complementar não encontrado!'}, 404

        if complementar['email'] != user_id:
            return {'message': 'Você não tem permissão para atualizar este cadastro!'}, 403

        # Apenas atualize os campos presentes em update_data
        update_fields = {key: value for key, value in update_data.items() if value is not None}

        if update_fields:
            result = self.cad_complementar.update_one(
                {'_id': ObjectId(complementar_id)},
                {'$set': update_fields}
            )

            if result.matched_count:
                return {'message': 'Cadastro complementar atualizado com sucesso!'}, 200

        return {'message': 'Nenhuma alteração realizada.'}, 400

    @jwt_required()
    def delete_complementar(self, complementar_id):
        result = self.cad_complementar.delete_one({'_id': ObjectId(complementar_id)})

        if result.deleted_count:
            return {'message': 'Cadastro complementar deletado com sucesso!'}, 200
        return {'message': 'Falha ao deletar o cadastro complementar!'}, 400
