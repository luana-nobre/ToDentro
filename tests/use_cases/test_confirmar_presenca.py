import pytest
from use_cases.confirmar_presenca import ConfirmarPresenca
from unittest.mock import MagicMock

def test_confirmar_presenca():
    role = MagicMock(titulo="Evento", participantes=[])
    repo = MagicMock()
    repo.listar.return_value = [role]
    use_case = ConfirmarPresenca(repo)

    use_case.execute("Evento", "usuario@email.com")

    assert "usuario@email.com" in role.participantes
    repo.salvar_todos.assert_called_once()