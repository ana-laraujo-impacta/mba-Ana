from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Importando os blueprints das rotas
from routers.auth_routes import auth_blueprint
from routers.faq_routes import faq_blueprint
from routers.pesquisa_routes import search_blueprint
from routers.cadastro_complementar_routes import cadastro_complementar_blueprint
from routers.user_cadastro_routes import user_cadastro_blueprint
from routers.imagens_perfil_routes import imagens_perfil_blueprint

load_dotenv()

app = Flask(__name__)

# Configuração do CORS para todas as rotas
CORS(app, origins="http://localhost:3000", supports_credentials=True, methods=["GET", "POST", "DELETE", "PUT"])

# Configurações JWT
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
jwt = JWTManager(app)

# Limite de upload de arquivos (16MB)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB

# Registrando os blueprints
app.register_blueprint(auth_blueprint)
app.register_blueprint(faq_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(user_cadastro_blueprint)
app.register_blueprint(cadastro_complementar_blueprint)
app.register_blueprint(imagens_perfil_blueprint)

# Rota inicial para testar a API
@app.route('/')
def home():
    return "API Flask com MongoDB"

# Executando a aplicação
if __name__ == '__main__':
    app.run(port=7000, host='localhost', debug=True)
