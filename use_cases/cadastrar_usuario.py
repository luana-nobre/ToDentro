from domain.usuario import Usuario
from infra.repositories.usuario_repository import UsuarioRepository

class CadastrarUsuario:
    def __init__(self):
        self.repo = UsuarioRepository()

    def executar(self, nome, email, senha, confirmacao):
        if senha != confirmacao:
            raise ValueError("As senhas não coincidem")
        
        novo = Usuario(nome, email, senha)
        self.repo.salvar(novo)
        return novo
