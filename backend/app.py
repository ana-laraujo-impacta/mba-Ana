from flask import Flask
from routers.routers import auth_blueprint, user_blueprint
from flask_jwt_extended import JWTManager
import os
from flask_cors import CORS


app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret_key'
# Registrar o blueprint
app.register_blueprint(auth_blueprint)
app.register_blueprint(user_blueprint)
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
CORS(app)
jwt = JWTManager(app)

@app.route('/')
def home():
    return "API Flask com MongoDB"

if __name__ == '__main__':
    app.run(port=7000,host='localhost',debug=True)
