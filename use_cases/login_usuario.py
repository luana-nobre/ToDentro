class LoginUsuario:
    def __init__(self, usuario_repository):
        self.repo = usuario_repository

    def execute(self, email: str, senha: str):
        return self.repo.buscar_por_email_senha(email, senha)
