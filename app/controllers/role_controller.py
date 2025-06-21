from flask import Blueprint, render_template, request, redirect, session, url_for
from use_cases.listar_roles import ListarRoles
from use_cases.criar_role import CriarRole
from use_cases.confirmar_presenca import ConfirmarPresenca
from use_cases.editar_role import EditarRole
from use_cases.apagar_role import ApagarRole
from use_cases.buscar_role_para_edicao import BuscarRoleParaEdicao
from infra.repositories.role_repository import RoleRepository

role_bp = Blueprint('role', __name__)
repo = RoleRepository()

@role_bp.route('/home', methods=['GET'])
def home():
    if 'usuario' not in session:
        return redirect(url_for('usuario.login'))

    use_case = ListarRoles(repo)
    filtro = request.args.get('filtro', 'todos')
    busca = request.args.get('busca', '')
    roles = use_case.execute(session['usuario'], session['email'], filtro, busca)

    return render_template('home.html', usuario=session['usuario'], roles=roles)

@role_bp.route('/criar-role', methods=['GET', 'POST'])
def criar_role():
    if 'usuario' not in session:
        return redirect(url_for('usuario.login'))

    if request.method == 'POST':
        use_case = CriarRole(repo)
        use_case.execute(
            request.form['titulo'],
            request.form['descricao'],
            request.form['data'],
            request.form['hora'],
            session['usuario']
        )
        return redirect(url_for('role.home'))

    return render_template('criar_role.html')

@role_bp.route('/confirmar/<titulo>', methods=['POST'])
def confirmar(titulo):
    if 'usuario' not in session:
        return redirect(url_for('usuario.login'))

    use_case = ConfirmarPresenca(repo)
    use_case.execute(titulo, session['email'])

    return redirect(url_for('role.home'))

@role_bp.route('/editar-role/<titulo>', methods=['GET', 'POST'])
def editar_role(titulo):
    if 'usuario' not in session:
        return redirect(url_for('usuario.login'))

    if request.method == 'POST':
        use_case = EditarRole(repo)
        novos_dados = {
            'titulo': request.form['titulo'],
            'descricao': request.form['descricao'],
            'data': request.form['data'],
            'hora': request.form['hora']
        }
        role = use_case.execute(titulo, session['usuario'], novos_dados)
        if role:
            return redirect(url_for('role.home'))
        return redirect(url_for('role.home'))

    use_case = BuscarRoleParaEdicao(repo)
    role = use_case.execute(titulo, session['usuario'])
    if not role:
        return redirect(url_for('role.home'))

    return render_template('criar_role.html', editar=True, role=role)

@role_bp.route('/apagar-role/<titulo>', methods=['POST'])
def apagar_role(titulo):
    if 'usuario' not in session:
        return redirect(url_for('usuario.login'))

    use_case = ApagarRole(repo)
    use_case.execute(titulo, session['usuario'])

    return redirect(url_for('role.home'))
