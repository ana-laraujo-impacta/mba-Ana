from flask import Flask
from routers.auth_routes import auth_blueprint
from routers.faq_routes import faq_blueprint
from routers.pesquisa_routes import search_blueprint
from routers.cadastro_complementar_routes import cadastro_complementar_blueprint
from routers.user_cadastro_routes import user_cadastro_blueprint
from routers.imagens_perfil_routes import imagens_perfil_blueprint

def register_routers(app: Flask):
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(faq_blueprint)
    app.register_blueprint(search_blueprint)
    app.register_blueprint(user_cadastro_blueprint)
    app.register_blueprint(cadastro_complementar_blueprint)
    app.register_blueprint(imagens_perfil_blueprint)
