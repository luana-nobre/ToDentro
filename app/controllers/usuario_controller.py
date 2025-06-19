from flask import Blueprint, render_template, request, redirect, session, url_for
from domain.usuario import UsuarioTeste
from infra.repositories.usuario_repository import UsuarioRepository


usuario_bp = Blueprint('usuario', __name__)
repo = UsuarioRepository()


@usuario_bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        usuario = repo.buscar_por_email_senha(email, senha)
        if usuario:
            session['usuario'] = usuario.nome
            session['email'] = usuario.email
            return redirect(url_for('role.home'))
        return render_template('login.html', erro="Credenciais inválidas")
    return render_template('login.html')


@usuario_bp.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        confirmar = request.form['confirmar']
        if senha != confirmar:
            return render_template('cadastro.html', erro="As senhas não coincidem")
        novo_usuario = UsuarioTeste(nome, email, senha)
        repo.salvar(novo_usuario)
        return redirect(url_for('usuario.login'))
    return render_template('cadastro.html')


@usuario_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('usuario.login'))
