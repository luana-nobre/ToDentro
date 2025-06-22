import pytest
from use_cases.editar_role import EditarRole
from unittest.mock import MagicMock

def test_editar_role():
    role = MagicMock(titulo="Antigo", criador="criador@email.com")
    repo = MagicMock()
    repo.listar.return_value = [role]
    use_case = EditarRole(repo)

    novos_dados = {
        "titulo": "Novo",
        "descricao": "Atualizada",
        "data": "2025-01-01",
        "hora": "09:00"
    }

    result = use_case.execute("Antigo", "criador@email.com", novos_dados)

    assert result.titulo == "Novo"
    assert result.descricao == "Atualizada"
    repo.salvar_todos.assert_called_once()