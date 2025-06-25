from domain.interfaces.role_repository_interface import RoleRepositoryInterface

class ListarRoles:
    def __init__(self, repo: RoleRepositoryInterface):
        self.repo = repo

    def execute(self, usuario, email_usuario, filtro="todos", busca=""):
        roles = list(reversed(self.repo.listar()))

        if filtro == "meus":
            roles = [r for r in roles if r.criador == usuario or email_usuario in r.participantes]

        if busca:
            roles = [r for r in roles if busca.lower() in r.titulo.lower()]

        return roles
