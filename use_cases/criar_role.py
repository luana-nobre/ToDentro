from domain.role import RoleTeste
# importa a entidade esperada pelo repositório


class CriarRole:
    def __init__(self, role_repository):
        self.repo = role_repository

    def execute(
            self,
            titulo: str,
            descricao: str,
            data: str,
            hora: str,
            criador: str
    ):
        role = RoleTeste(titulo, descricao, data, hora, criador, [])
        self.repo.salvar(role)
        return role
