import pytest
from use_cases.criar_role import CriarRole
from unittest.mock import MagicMock

def test_criar_role():
    repo = MagicMock()
    use_case = CriarRole(repo)

    result = use_case.execute("Título", "Desc", "2025-01-01", "10:00", "criador@email.com")

    repo.salvar.assert_called_once()
    assert result.titulo == "Título"
    assert result.descricao == "Desc"
    assert result.criador == "criador@email.com"