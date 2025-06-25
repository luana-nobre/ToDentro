from domain.interfaces.usuario_repository_interface import (
    UsuarioRepositoryInterface
)


class LoginUsuario:
    def __init__(self, repo: UsuarioRepositoryInterface):
        self.repo = repo

    def execute(self, email, senha):
        return self.repo.buscar_por_email_senha(email, senha)
