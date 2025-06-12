# main.py
from flask import Flask, render_template, request, redirect, session, url_for
from app.controllers.usuario_controller import usuario_bp
from app.controllers.role_controller import role_bp
import os


app = Flask(__name__)
app.secret_key = 'segredo'

# Blueprint routes
app.register_blueprint(usuario_bp)
app.register_blueprint(role_bp)

if __name__ == '__main__':
    os.makedirs('app/templates', exist_ok=True)
    open('usuario.txt', 'a').close()
    open('role.txt', 'a').close()
    app.run(debug=True)
