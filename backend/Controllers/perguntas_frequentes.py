###opcional, so get
##end point:/perguntas,               ##@app.route('/livros/<int:id>',methods=['GET'])

from flask import jsonify

class FaqController:
    def __init__(self, db):
        self.faq_collection = db['faq']

    def get_all_faqs(self):
        faqs = self.faq_collection.find({}, {'_id': 1, 'pergunta': 1, 'resposta': 1})
        result = []
        for faq in faqs:
            result.append({
                '_id': str(faq['_id']),
                'pergunta': faq['pergunta'],
                'resposta': faq['resposta']
            })
        self.faq_collection.find()
        return jsonify(result), 200

    def add_faq(self, pergunta, resposta):
            faq = {'pergunta': pergunta, 'resposta': resposta}
            result = self.faq_collection.insert_one(faq)
            return jsonify({'message': 'FAQ adicionado com sucesso!', 'id': str(result.inserted_id)}), 201