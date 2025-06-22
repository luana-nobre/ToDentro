import pytest
from use_cases.cadastrar_usuario import CadastrarUsuario
from unittest.mock import MagicMock

def test_cadastrar_usuario_sucesso():
    repo = MagicMock()
    use_case = CadastrarUsuario(repo)

    result = use_case.execute("João", "joao@email.com", "senha123", "senha123")

    repo.salvar.assert_called_once()
    assert result["nome"] == "João"
    assert result["email"] == "joao@email.com"

def test_cadastrar_usuario_senhas_diferentes():
    repo = MagicMock()
    use_case = CadastrarUsuario(repo)

    with pytest.raises(ValueError, match="As senhas não coincidem"):
        use_case.execute("João", "joao@email.com", "senha123", "outra")