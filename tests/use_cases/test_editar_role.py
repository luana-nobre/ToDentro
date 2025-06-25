from use_cases.editar_role import EditarRole
from unittest.mock import MagicMock
from domain.role import RoleTeste


def test_editar_role():
    role = RoleTeste(
        "Antigo", "Desc", "2025-01-01", "08:00",
        "criador@email.com", []
    )
    repo = MagicMock()
    repo.listar.return_value = [role]
    use_case = EditarRole(repo)

    novos = {
        "titulo": "Novo",
        "descricao": "Atualizada",
        "data": "2025-01-01",
        "hora": "09:00",
    }

    result = use_case.execute("Antigo", role.criador, novos)

    assert result.titulo == "Novo"
    repo.salvar_todos.assert_called_once()
