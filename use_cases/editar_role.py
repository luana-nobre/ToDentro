class EditarRole:
    def __init__(self, role_repository):
        self.repo = role_repository

    def execute(self, titulo: str, usuario: str, novos_dados: dict):
        roles = self.repo.listar()
        role = next((r for r in roles if r.titulo == titulo), None)
        if not role or role.criador != usuario:
            return None
        role.titulo = novos_dados["titulo"]
        role.descricao = novos_dados["descricao"]
        role.data = novos_dados["data"]
        role.hora = novos_dados["hora"]
        self.repo.salvar_todos(roles)
        return role
