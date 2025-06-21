from use_cases.listar_roles import ListarRoles
from domain.role import RoleTeste


def fake_roles():
    return [
        RoleTeste("Festa 1", "desc", "data", "hora", "João", ["email1"]),
        RoleTeste("Festa 2", "desc", "data", "hora", "Maria", ["email2"])
    ]


class FakeRepo:
    def listar(self):
        return fake_roles()


def test_listar_todos():
    caso_uso = ListarRoles()
    caso_uso.repo = FakeRepo()
    resultado = caso_uso.executar()
    assert len(resultado) == 2


def test_filtrar_meus_roles():
    caso_uso = ListarRoles()
    caso_uso.repo = FakeRepo()
    resultado = caso_uso.executar(
        filtro="meus", usuario_nome="João", usuario_email="email1")
    assert len(resultado) == 1
    assert resultado[0].criador == "João"
