from domain.role import RoleTeste
from domain.interfaces.role_repository_interface import RoleRepositoryInterface


class CriarRole:
    def __init__(self, repo: RoleRepositoryInterface):
        self.repo = repo

    def execute(self, titulo, descricao, data, hora, criador):
        role = RoleTeste(titulo, descricao, data, hora, criador, [])
        self.repo.salvar(role)
        return role
