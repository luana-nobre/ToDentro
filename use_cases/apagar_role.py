from domain.interfaces.role_repository_interface import RoleRepositoryInterface


class ApagarRole:
    def __init__(self, repo: RoleRepositoryInterface):
        self.repo = repo

    def execute(self, id, email_usuario):
        roles = self.repo.listar()
        novas_roles = [
            r
            for r in roles
            if not (
                r.titulo == id and
                r.criador == email_usuario
            )
        ]
        self.repo.salvar_todos(novas_roles)
