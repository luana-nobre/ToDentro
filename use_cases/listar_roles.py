class ListarRoles:
    def __init__(self, role_repository):
        self.repo = role_repository

    def execute(
            self,
            usuario: str,
            email_usuario: str,
            filtro: str = 'todos',
            busca: str = ''
    ):
        roles = list(reversed(self.repo.listar()))

        if filtro == 'meus':
            roles = [
                r for r in roles
                if r.get('criador') == usuario or
                email_usuario in r.get('participantes', [])
            ]

        if busca:
            roles = [
                r for r in roles
                if busca.lower() in r.get('titulo', '').lower()
            ]

        return roles
