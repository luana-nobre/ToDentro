from use_cases.buscar_role_para_edicao import BuscarRoleParaEdicao
from unittest.mock import MagicMock


def test_buscar_role_para_edicao_encontrada():
    role = MagicMock(titulo="Role A", criador="usuario@email.com")
    repo = MagicMock()
    repo.listar.return_value = [role]
    use_case = BuscarRoleParaEdicao(repo)

    result = use_case.execute("Role A", "usuario@email.com")

    assert result == role


def test_buscar_role_para_edicao_nao_encontrada():
    repo = MagicMock()
    repo.listar.return_value = []
    use_case = BuscarRoleParaEdicao(repo)

    result = use_case.execute("Role Inexistente", "usuario@email.com")

    assert result is None
