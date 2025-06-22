from sqlalchemy import (
    create_engine,
    Column, String,
    Integer
)  # , ForeignKey  #vai criar o banco de dados mas a cria vazia
from sqlalchemy.orm import (
    sessionmaker,
    declarative_base
)  # orm: object related mapping


db = create_engine("sqlite:///meubanco.db")
# link do banco de dados. Cria um banco de dados ou conecta com um já existente
Session = sessionmaker(bind=db)
# o bind diz o nome do banco de dados (que foi criado a partir da variável db)
session = Session()


def get_session():
    return Session()


Base = declarative_base()

# criação das tabelas


class Usuario (Base):
    __tablename__ = "usuarios"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    # nao vai ser passado no init será criado automaticamente pela tabela.
    # Ou seja, ao criar um usuario eu nao vou passar o id dele
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


class Role(Base):
    __tablename__ = "roles"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    # autoincrement=True -> id atual sempre vai ser maior que o id anterior
    titulo = Column("titulo", String)
    descricao = Column("descricao", String)
    data = Column("data", String)
    hora = Column("hora", String)
    # criador = Column("criador", ForeignKey=True)
    criador = Column("criador", String)
    # participantes = Column("participantes", ForeignKey=True)
    participantes = Column("participantes", String)

    def __init__(self, titulo, descricao, data, hora, criador, participantes):
        self.titulo = titulo
        self.descricao = descricao
        self.data = data
        self.hora = hora
        self.criador = criador
        self.participantes = participantes


Base.metadata.create_all(bind=db)

# quando criamos as tabelas e colunas, elas devem ter regras.
# Ex: coluna nunca pode ser vazia
# primary key -> valor único identifica tupla no banco
# C(reate)R(ead)U(pdate)D(elete)

# para criar usuários:
usuario1 = Usuario(
    nome="Isabela Braconi Pontual",
    email="belabpontual@gmail.com",
    senha="viv@Brasília"
)

# para adicionar usuarios:
# session.add(usuario1)

# salvar a sessao no banco de dados:
# session.commit()

usuario2 = Usuario(
    nome="Luana Nobre",
    email="luananobre@gmail.com",
    senha="lu@ninh@"
)
# session.add(usuario2)
# session.commit()

usuario3 = Usuario(
    nome="João Marcelo",
    email="joaomarceloonofre@gmail.com",
    senha="jpm12345"
)
# session.add(usuario3)
# session.commit()

usuario4 = Usuario(
    nome="Paulo Henrique",
    email="phPuc@gmail.com",
    senha="ph123"
)
# session.add(usuario4)
# session.commit()

usuario5 = Usuario(
    nome="João Pedro Feijó",
    email="jpfeijo@gmail.com",
    senha="jpf_tropadoKwid"
)
# session.add(usuario5)
# session.commit()

role1 = Role(
    titulo="Casa do Feijó",
    descricao="Rua Venâncio Flores 225",
    data="05/07/2025", hora="19:00",
    criador="João Pedro Feijó",
    participantes="João Pedro Feijó, Isabela Braconi, Luana Nobre"
)
# session.add(role1)
# session.commit()
role2 = Role(
    titulo="Casa da Bela",
    descricao="Rua Jardim Botânico 496",
    data="21/07/2025",
    hora="16:00",
    criador="Isabela Braconi Pontual",
    participantes="Isabela Braconi Pontual, Luana Nobre"
)
# session.add(role2)
# session.commit()
role3 = Role(
    titulo="Casa do Paulete",
    descricao="Avenida das Américas 140",
    data="16/08/2025", hora="14:00",
    criador="Paulo Henrique",
    participantes="Paulo Henrique, João Marcelo, João Pedro Feijó"
)
# session.add(role3)
# session.commit()
role4 = Role(
    titulo="Casa do JM",
    descricao="Rua Ataulfo de Paiva",
    data="02/05/2025",
    hora="20:00",
    criador="João Marcelo",
    participantes=(
        "Isabela Braconi Pontual,"
        "Luana Nobre,"
        "Paulo Henrique,"
        "João Marcelo,"
        "João Pedro Feijó"
    )
)
# session.add(role4)
# session.commit()
role5 = Role(
    titulo="Casa da Lulu",
    descricao="Rua Rainha Guilhermina",
    data="30/01/2025",
    hora="12:00",
    criador="Luana Nobre",
    participantes="Luana Nobre, Isabela Braconi"
)
# session.add(role5)
# session.commit()

# Para Delete:
# session.query(Role).delete()   # gera DELETE FROM usuarios;
# session.commit()
