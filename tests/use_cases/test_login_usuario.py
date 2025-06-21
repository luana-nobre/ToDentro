import pytest
from use_cases.login_usuario import LoginUsuario
from domain.usuario import UsuarioTeste


class FakeRepo:
    def buscar_por_email_senha(self, email, senha):
        if email == "teste@exemplo.com" and senha == "senha123":
            return UsuarioTeste("Teste", email, senha)
        return None


def test_login_sucesso():
    caso_uso = LoginUsuario()
    caso_uso.repo = FakeRepo()
    usuario = caso_uso.executar("teste@exemplo.com", "senha123")
    assert usuario is not None
    assert usuario.nome == "Teste"


def test_login_falha():
    caso_uso = LoginUsuario()
    caso_uso.repo = FakeRepo()
    usuario = caso_uso.executar("teste@exemplo.com", "errada")
    assert usuario is None
