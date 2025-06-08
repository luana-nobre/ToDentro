from app.entities.role import Role

class RoleRepository:
    ARQUIVO = 'role.txt'

    def salvar(self, role):
        with open(self.ARQUIVO, "a") as f:
            f.write(role.to_line())

    def listar(self):
        roles = []
        try:
            with open(self.ARQUIVO, "r") as f:
                roles = [Role.from_line(line) for line in f]
        except FileNotFoundError:
            pass
        return roles

    def salvar_todos(self, lista_roles):
        with open(self.ARQUIVO, "w") as f:
            for r in lista_roles:
                f.write(r.to_line())
