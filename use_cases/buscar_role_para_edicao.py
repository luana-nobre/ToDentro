from domain.interfaces.role_repository_interface import RoleRepositoryInterface


class BuscarRoleParaEdicao:
    def __init__(self, repo: RoleRepositoryInterface):
        self.repo = repo

    def execute(self, titulo, criador):
        roles = self.repo.listar()
        for role in roles:
            if role.titulo == titulo and role.criador == criador:
                return role
        return None
