from use_cases.apagar_role import ApagarRole
from unittest.mock import MagicMock


def test_apagar_role():
    repo = MagicMock()
    repo.listar.return_value = [
        MagicMock(
            titulo="Evento",
            criador="usuario@email.com"
        )
    ]
    use_case = ApagarRole(repo)

    use_case.execute("Evento", "usuario@email.com")

    repo.salvar_todos.assert_called_once()
