from domain.interfaces.role_repository_interface import RoleRepositoryInterface


class EditarRole:
    def __init__(self, repo: RoleRepositoryInterface):
        self.repo = repo

    def execute(self, titulo_original, email_usuario, novos_dados):
        roles = self.repo.listar()
        for role in roles:
            if role.titulo == titulo_original and role.criador == email_usuario:
                role.titulo = novos_dados["titulo"]
                role.descricao = novos_dados["descricao"]
                role.data = novos_dados["data"]
                role.hora = novos_dados["hora"]
                self.repo.salvar_todos(roles)
                return role

        return None
