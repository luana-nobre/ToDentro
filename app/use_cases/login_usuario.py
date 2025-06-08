from app.interface_adapters.usuario_repository import UsuarioRepository

class LoginUsuario:
    def __init__(self):
        self.repo = UsuarioRepository()

    def executar(self, email, senha):
        return self.repo.buscar_por_email_senha(email, senha)
