import pytest
from use_cases.listar_roles import ListarRoles
from unittest.mock import MagicMock

def test_listar_roles_padrao():
    repo = MagicMock()
    repo.listar.return_value = [
        {"titulo": "Evento", "criador": "Usuario"},
        {"titulo": "Outro"}
    ]
    use_case = ListarRoles(repo)

    result = use_case.execute("Usuario", "usuario@email.com")

    assert isinstance(result, list)
    assert len(result) == 2

def test_listar_roles_filtrados():
    repo = MagicMock()
    repo.listar.return_value = [
        {"titulo": "Evento", "criador": "Usuario", "participantes": []},
        {"titulo": "Outro", "criador": "Outro", "participantes": ["usuario@email.com"]}
    ]
    use_case = ListarRoles(repo)

    result = use_case.execute("Usuario", "usuario@email.com", filtro="meus")

    assert len(result) == 2