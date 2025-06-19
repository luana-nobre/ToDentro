from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    session,
    url_for
)
from app.entities.role import Role
from app.interface_adapters.role_repository import RoleRepository


role_bp = Blueprint('role', __name__)
repo = RoleRepository()


@role_bp.route('/home', methods=['GET'])
def home():
    if 'usuario' not in session:
        return redirect(url_for('usuario.login'))
    roles = list(reversed(repo.listar()))
    filtro = request.args.get('filtro', 'todos')
    email_usuario = session['email']
    if filtro == 'meus':
        roles = [
            r for r in roles
            if r.criador == session['usuario']
            or email_usuario in r.participantes
        ]
    busca = request.args.get('busca', '').lower()
    if busca:
        roles = [
            r for r in roles
            if busca in r.titulo.lower()
        ]
    return render_template(
        'home.html',
        usuario=session['usuario'],
        roles=roles
    )


@role_bp.route('/criar-role', methods=['GET', 'POST'])
def criar_role():
    if 'usuario' not in session:
        return redirect(url_for('usuario.login'))
    if request.method == 'POST':
        titulo = request.form['titulo']
        descricao = request.form['descricao']
        data = request.form['data']
        hora = request.form['hora']
        novo = RoleTeste(titulo, descricao, data, hora, session['usuario'])
        repo.salvar(novo)
        return redirect(url_for('role.home'))
    return render_template('criar_role.html')


@role_bp.route('/confirmar/<titulo>', methods=['POST'])
def confirmar(titulo):
    if 'usuario' not in session:
        return redirect(url_for('usuario.login'))
    email_usuario = session['email']
    roles = repo.listar()
    for r in roles:
        if r.titulo == titulo and email_usuario not in r.participantes:
            r.participantes.append(email_usuario)
            break
    repo.salvar_todos(roles)
    return redirect(url_for('role.home'))


@role_bp.route('/editar-role/<titulo>', methods=['GET', 'POST'])
def editar_role(titulo):
    if 'usuario' not in session:
        return redirect(url_for('usuario.login'))

    roles = repo.listar()
    role = next((r for r in roles if r.titulo == titulo), None)

    if not role or role.criador != session['usuario']:
        return redirect(url_for('role.home'))

    if request.method == 'POST':
        role.titulo = request.form['titulo']
        role.descricao = request.form['descricao']
        role.data = request.form['data']
        role.hora = request.form['hora']
        repo.salvar_todos(roles)
        return redirect(url_for('role.home'))

    return render_template(
        'criar_role.html',
        editar=True,
        role=role
    )


@role_bp.route('/apagar-role/<titulo>', methods=['POST'])
def apagar_role(titulo):
    if 'usuario' not in session:
        return redirect(url_for('usuario.login'))

    roles = repo.listar()
    novas = [
        r for r in roles
        if not (
            r.titulo == titulo and
            r.criador == session['usuario']
        )
    ]
    repo.salvar_todos(novas)

    return redirect(url_for('role.home'))
