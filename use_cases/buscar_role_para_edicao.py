class BuscarRoleParaEdicao:
    def __init__(self, role_repository):
        self.repo = role_repository

    def execute(self, titulo: str, usuario: str):
        roles = self.repo.listar()
        role = next((r for r in roles if r.titulo == titulo), None)
        if not role or role.criador != usuario:
            return None
        return role
