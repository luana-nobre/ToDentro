class RoleTeste:
    def __init__(self, titulo, descricao, data, hora, criador, participantes=None):
        self.titulo = titulo
        self.descricao = descricao
        self.data = data
        self.hora = hora
        self.criador = criador
        self.participantes = participantes if participantes else []

    def to_line(self):
        participantes_str = ",".join(self.participantes)
        return (
            f"{self.titulo};{self.descricao};{self.data};"
            f"{self.hora};{self.criador};{participantes_str}\n"
        )

    @staticmethod
    def from_line(line):
        titulo, desc, data, hora, criador, part_str = line.strip().split(";")
        participantes = part_str.split(",") if part_str else []
        return RoleTeste(titulo, desc, data, hora, criador, participantes)