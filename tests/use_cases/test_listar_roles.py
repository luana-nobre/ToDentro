from use_cases.listar_roles import ListarRoles
from unittest.mock import MagicMock
from domain.role import RoleTeste


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
        RoleTeste("Evento", "desc", "2025-01-01", "10:00", "Usuario", []),
        RoleTeste(
            "Outro", "desc", "2025-01-02", "11:00",
            "Outro", ["usuario@email.com"]
        ),
    ]
    use_case = ListarRoles(repo)

    result = use_case.execute(
        "Usuario", "usuario@email.com", filtro="meus"
    )

    assert len(result) == 2
    assert {r.titulo for r in result} == {"Evento", "Outro"}
