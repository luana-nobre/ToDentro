from app.entities.usuario import Usuario

class UsuarioRepository:
    ARQUIVO = 'usuario.txt'

    def salvar(self, usuario):
        with open(self.ARQUIVO, "a") as f:
            f.write(usuario.to_line())

    def buscar_por_email_senha(self, email, senha):
        with open(self.ARQUIVO, "r") as f:
            for line in f:
                u = Usuario.from_line(line)
                if u.email == email and u.senha == senha:
                    return u
        return None
