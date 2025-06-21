import pytest
from use_cases.cadastrar_usuario import CadastrarUsuario
from domain.usuario import UsuarioTeste


class FakeRepo:
    def __init__(self):
        self.salvo = None

    def salvar(self, usuario):
        self.salvo = usuario


def test_cadastro_sucesso():
    caso_uso = CadastrarUsuario()
    caso_uso.repo = FakeRepo()
    usuario = caso_uso.executar("João", "joao@email.com", "1234", "1234")
    assert usuario.nome == "João"
    assert caso_uso.repo.salvo.email == "joao@email.com"


def test_cadastro_erro_confirmacao():
    caso_uso = CadastrarUsuario()
    with pytest.raises(ValueError):
        caso_uso.executar("João", "joao@email.com", "1234", "diferente")
