# main.py
from flask import Flask, render_template, request, redirect, session, url_for
from app.controllers.usuario_controller import usuario_bp
from app.controllers.role_controller import role_bp
import os

app = Flask(__name__,
            template_folder='templates',
            static_folder='static')

app.secret_key = 'segredo'

# Blueprint routes
app.register_blueprint(usuario_bp)
app.register_blueprint(role_bp)

if __name__ == '__main__':
    os.makedirs('templates', exist_ok=True)
    app.run(debug=True)
    
    # app/main.py  (trecho final)

from infra.repositories.usuario_repository import UsuarioRepository
from infra.repositories.role_repository import RoleRepository

if __name__ == "__main__":
    # ----- DEBUG: imprime estado atual do banco -----
    print("====== DEBUG DB ======")

    usuarios = UsuarioRepository().listar()
    print(f"Usuários ({len(usuarios)}):")
    for u in usuarios:
        print("  -", u)

    roles = RoleRepository().listar()
    print(f"\nRoles ({len(roles)}):")
    for r in roles:
        print("  -", r)

    print("======================\n")
    # ----- Fim do bloco de debug -----

    app.run(debug=True)