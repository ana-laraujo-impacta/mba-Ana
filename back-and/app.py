from flask import Flask
from routers.routers import auth_blueprint

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
# Registrar o blueprint
app.register_blueprint(auth_blueprint)

if __name__ == '__main__':
    app.run(port=5000,host='localhost',debug=True)
