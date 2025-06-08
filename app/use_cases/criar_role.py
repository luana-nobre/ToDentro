from app.entities.role import Role
from app.interface_adapters.role_repository import RoleRepository

class CriarRole:
    def __init__(self):
        self.repo = RoleRepository()

    def executar(self, titulo, descricao, data, hora, criador):
        novo = Role(titulo, descricao, data, hora, criador)
        self.repo.salvar(novo)
        return novo
