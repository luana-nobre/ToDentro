class UsuarioTeste:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha  # em produção, seria hash

    def to_line(self):
        return f"{self.nome};{self.email};{self.senha}\n"

    @staticmethod
    def from_line(line):
        nome, email, senha = line.strip().split(";")
        return UsuarioTeste(nome, email, senha)