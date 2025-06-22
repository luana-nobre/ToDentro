from use_cases.login_usuario import LoginUsuario
from unittest.mock import MagicMock


def test_login_sucesso():
    repo = MagicMock()
    repo.buscar_por_email_senha.return_value = MagicMock(
        nome="Teste",
        email="teste@email.com",
        senha="123"
    )
    use_case = LoginUsuario(repo)

    result = use_case.execute("teste@email.com", "123")

    repo.buscar_por_email_senha.assert_called_once_with(
        "teste@email.com",
        "123"
    )
    assert result is not None
    assert result.email == "teste@email.com"


def test_login_falha():
    repo = MagicMock()
    repo.buscar_por_email_senha.return_value = None
    use_case = LoginUsuario(repo)

    result = use_case.execute("invalido@email.com", "senhaerrada")

    repo.buscar_por_email_senha.assert_called_once_with(
        "invalido@email.com",
        "senhaerrada"
    )
    assert result is None
