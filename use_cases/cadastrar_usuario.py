class CadastrarUsuario:
    def __init__(self, usuario_repository):
        self.repo = usuario_repository

    def execute(self, nome: str, email: str, senha: str, confirmar: str):
        if senha != confirmar:
            raise ValueError("As senhas não coincidem")

        usuario = {
            "nome": nome,
            "email": email,
            "senha": senha
        }

        self.repo.salvar(usuario)
        return usuario
