from app.interface_adapters.role_repository import RoleRepository


class ConfirmarPresenca:
    def __init__(self):
        self.repo = RoleRepository()

    def executar(self, titulo_role, email_usuario):
        roles = self.repo.listar()
        for role in roles:
            if (
                role.titulo == titulo_role and
                email_usuario not in role.participantes
            ):
                role.participantes.append(email_usuario)
                break
        self.repo.salvar_todos(roles)
