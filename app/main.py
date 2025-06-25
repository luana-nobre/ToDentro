from flask import Flask
from app.controllers.usuario_controller import usuario_bp
from app.controllers.role_controller import role_bp
import os

app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = 'segredo'

# Blueprint routes
app.register_blueprint(usuario_bp)
app.register_blueprint(role_bp)

if __name__ == '__main__':
    # Criação de pasta templates (evita erro se não existir)
    os.makedirs('templates', exist_ok=True)

    app.run(debug=True)
