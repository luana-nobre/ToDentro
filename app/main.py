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

# ────────────────────────────────────────────────────────────────────────────────
# Repositórios concretos (infraestrutura – SQLAlchemy)
# ────────────────────────────────────────────────────────────────────────────────
from infra.repositories.role_repository import RoleRepository
from infra.repositories.usuario_repository import UsuarioRepository

# Controladores (camada de interface / apresentação)
# Obs.: o import vem **depois** dos repositórios para permitir a injeção.
from app.controllers import role_controller, usuario_controller


def create_app() -> Flask:
    """
    Factory principal da aplicação.
    Retorna um objeto `Flask` totalmente configurado.
    """
    # 1 ▸ Flask App
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.secret_key = "segredo"  # ➜ substitua em produção

    # 2 ▸ Instancia os repositórios concretos (SQLAlchemy)
    role_repo = RoleRepository()
    usuario_repo = UsuarioRepository()

    # 3 ▸ Injeta dependências nos controladores
    #
    # ─ Como os controladores usam a variável global `repo`, basta sobrescrevê-la
    #   ANTES de registrar o blueprint. A cada requisição o controlador
    #   acessará o mesmo objeto — singleton simples.
    role_controller.repo = role_repo
    usuario_controller.repo = usuario_repo

    # 4 ▸ Registro dos blueprints já configurados
    app.register_blueprint(usuario_controller.usuario_bp)
    app.register_blueprint(role_controller.role_bp)

    # --------------------------------------------------------------------------
    # 5 ▸ Qualquer outra dependência global pode ser injetada aqui
    # --------------------------------------------------------------------------

    return app


# ────────────────────────────────────────────────────────────────────────────────
# Execução como script (`python app/main.py`)
# ────────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # Garante que a pasta de templates exista (evita erros em primeiras execuções)
    os.makedirs("templates", exist_ok=True)

    flask_app = create_app()
    # DEBUG: imprime algo útil, se desejar
    # print("====== DEBUG DB ======")

    # Inicia a aplicação
    flask_app.run(debug=True)
