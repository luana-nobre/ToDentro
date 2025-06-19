from infra.repositories.role_repository import RoleRepository


class ListarRoles:
    def __init__(self):
        self.repo = RoleRepository()

    def executar(
            self,
            filtro='todos',
            usuario_nome=None,
            usuario_email=None,
            busca=''
            ):
        roles = self.repo.listar()

        if filtro == 'meus' and usuario_nome and usuario_email:
            roles = [
                r for r in roles
                if r.criador == usuario_nome
                or usuario_email in r.participantes
            ]

        if busca:
            roles = [r for r in roles if busca.lower() in r.titulo.lower()]

        return roles
