from use_cases.criar_role import CriarRole
from domain.role import RoleTeste


class FakeRepo:
    def __init__(self):
        self.salvo = None

    def salvar(self, role):
        self.salvo = role


def test_criar_role_sucesso():
    caso_uso = CriarRole()
    caso_uso.repo = FakeRepo()
    role = caso_uso.executar(
        "Festa", "Na praia", "2025-07-10", "20:00", "João")
    assert role.titulo == "Festa"
    assert caso_uso.repo.salvo.descricao == "Na praia"
