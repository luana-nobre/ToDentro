from domain.role import Role
from infra.repositories.role_repository import RoleRepository


class CriarRole:
    def __init__(self):
        self.repo = RoleRepository()

    def executar(self, titulo, descricao, data, hora, criador):
        novo = Role(titulo, descricao, data, hora, criador)
        self.repo.salvar(novo)
        return novo
