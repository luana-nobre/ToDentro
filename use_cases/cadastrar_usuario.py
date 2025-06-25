from domain.interfaces.usuario_repository_interface import (
    UsuarioRepositoryInterface
)
from domain.usuario import UsuarioTeste


class CadastrarUsuario:
    def __init__(self, repo: UsuarioRepositoryInterface):
        self.repo = repo

    def execute(self, nome, email, senha, confirmar):
        if senha != confirmar:
            raise ValueError("As senhas não coincidem")

        usuario = UsuarioTeste(nome, email, senha)
        self.repo.salvar(usuario)
        return usuario
