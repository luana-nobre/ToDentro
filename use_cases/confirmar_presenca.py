from domain.interfaces.role_repository_interface import RoleRepositoryInterface


class ConfirmarPresenca:
    def __init__(self, repo: RoleRepositoryInterface):
        self.repo = repo

    def execute(self, titulo, email_usuario):
        roles = self.repo.listar()
        for role in roles:
            if (
                role.titulo == titulo and
                email_usuario not in role.participantes
            ):
                role.participantes.append(email_usuario)
                break
        self.repo.salvar_todos(roles)
