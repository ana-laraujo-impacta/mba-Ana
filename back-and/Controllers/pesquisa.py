##get(especificar o bairro e a cidade[end points])
##endpoint: /pesquisa/bairro/cidade
##ana

from flask import jsonify

class UserController:
    def __init__(self, db):
        self.users_collection = db['cad_usuario']

    def search_users_by_location(self, latitude, longitude, cidade=None, bairro=None):
        # Defina um raio de pesquisa (em graus de latitude/longitude) - exemplo de 0.1 graus
        # radius = 0.1
        
        # # Converta latitude e longitude em coordenadas mínimas e máximas
        # lat_min = latitude - radius
        # lat_max = latitude + radius
        # lon_min = longitude - radius
        # lon_max = longitude + radius

        # # Crie o filtro de consulta
        # query = {
        #     'tp_cad': {'$in': [2, 3]},
        #     'latitude': {'$gte': lat_min, '$lte': lat_max},
        #     'longitude': {'$gte': lon_min, '$lte': lon_max}
        # }

        query = {
            'tp_cad': {'$in': [1, 2, 3]}
        }

        if cidade:
            query['cidade'] = cidade
        if bairro:
            query['bairro'] = bairro

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
