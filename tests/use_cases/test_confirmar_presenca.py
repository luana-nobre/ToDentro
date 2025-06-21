from use_cases.confirmar_presenca import ConfirmarPresenca
from domain.role import RoleTeste

class FakeRepo:
    def __init__(self):
        self.roles = [
            RoleTeste("Festa", "desc", "data", "hora", "João", ["email1"])
        ]

    def listar(self):
        return self.roles

    def salvar_todos(self, roles):
        self.salvo = roles


def test_confirmar_presenca_sucesso():
    caso_uso = ConfirmarPresenca()
    caso_uso.repo = FakeRepo()
    caso_uso.executar("Festa", "email2")
    assert "email2" in caso_uso.repo.salvo[0].participantes
