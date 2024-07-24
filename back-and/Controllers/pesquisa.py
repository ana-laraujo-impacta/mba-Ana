##get(especificar o bairro e a cidade[end points])
##endpoint: /pesquisa/bairro/cidade
##ana

from flask import jsonify
import unicodedata

def normalize_string(s):
    return unicodedata.normalize('NFKD', s).encode('ASCII', 'ignore').decode('ASCII').lower()

class UserController:
    def __init__(self, db):
        self.users_collection = db['cad_usuario']

    def get_all_users(self):
        users = self.users_collection.find({}, {'_id': 1, 'nome': 1, 'cidade': 1, 'bairro': 1})
        result = []
        for user in users:
            result.append({
                '_id': str(user['_id']),
                'nome': user.get('nome'),
                'cidade': user.get('cidade'),
                'bairro': user.get('bairro')
            })
        return jsonify(result), 200

    def search_users_by_location(self, cidade=None, bairro=None):
            query = {
                'tp_cad': {'$in': [2, 3]}
            }

            if cidade:
                query['cidade'] = normalize_string(cidade)
            if bairro:
                query['bairro'] = normalize_string(bairro)

            print(f"Query MongoDB: {query}")  # Debugging

            users = self.users_collection.find(query, {'_id': 1, 'nome': 1, 'cidade': 1, 'bairro': 1})
            result = []
            for user in users:
                result.append({
                    '_id': str(user['_id']),
                    'nome': user.get('nome'),
                    'cidade': user.get('cidade'),
                    'bairro': user.get('bairro')
                })
            return jsonify(result), 200
