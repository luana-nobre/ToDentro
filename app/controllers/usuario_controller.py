from flask import Blueprint, render_template, request, redirect, session, url_for
from use_cases.login_usuario import LoginUsuario
from use_cases.cadastrar_usuario import CadastrarUsuario
from infra.repositories.usuario_repository import UsuarioRepository

usuario_bp = Blueprint('usuario', __name__)
repo = UsuarioRepository()

@usuario_bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        use_case = LoginUsuario(repo)
        usuario = use_case.execute(email, senha)
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
        try:
            use_case = CadastrarUsuario(repo)
            use_case.execute(nome, email, senha, confirmar)
            return redirect(url_for('usuario.login'))
        except ValueError as e:
            return render_template('cadastro.html', erro=str(e))
    return render_template('cadastro.html')


@usuario_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('usuario.login'))
