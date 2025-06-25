# app/main.py
"""
Ponto de entrada da aplicação Flask.

Neste módulo acontecem:
1. Criação do objeto `Flask`.
2. Instanciação dos repositórios concretos (SQLAlchemy).
3. Injeção desses repositórios nos controladores.
4. Registro dos blueprints resultantes.
"""

import os
from flask import Flask
from infra.repositories.role_repository import RoleRepository
from infra.repositories.usuario_repository import UsuarioRepository
from app.controllers import role_controller, usuario_controller


def create_app() -> Flask:

    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.secret_key = "segredo"

    role_repo = RoleRepository()
    usuario_repo = UsuarioRepository()

    role_controller.repo = role_repo
    usuario_controller.repo = usuario_repo

    app.register_blueprint(usuario_controller.usuario_bp)
    app.register_blueprint(role_controller.role_bp)

    return app


if __name__ == "__main__":
    os.makedirs("templates", exist_ok=True)

    flask_app = create_app()

    # Inicia a aplicação
    flask_app.run(debug=True)
