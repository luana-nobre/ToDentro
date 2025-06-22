class ConfirmarPresenca:
    def __init__(self, role_repository):
        self.repo = role_repository

    def execute(self, titulo: str, email_usuario: str):
        roles = self.repo.listar()
        for r in roles:
            if r.titulo == titulo and email_usuario not in r.participantes:
                r.participantes.append(email_usuario)
                break
        self.repo.salvar_todos(roles)
