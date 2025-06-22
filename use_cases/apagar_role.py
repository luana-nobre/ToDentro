class ApagarRole:
    def __init__(self, role_repository):
        self.repo = role_repository

    def execute(self, titulo: str, usuario: str):
        roles = self.repo.listar()
        novas = [
            r for r in roles if not (
                r.titulo == titulo and
                r.criador == usuario
            )
        ]
        self.repo.salvar_todos(novas)
