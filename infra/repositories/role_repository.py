# app/infra/repositories/role_repository.py
from typing import List
from domain.role import RoleTeste
from infra.db.database import get_session, Role


class RoleRepository:
    ARQUIVO = None

    def salvar(self, role: RoleTeste) -> None:
        with get_session() as db:
            db.add(Role(
                titulo=role.titulo,
                descricao=role.descricao,
                data=role.data,
                hora=role.hora,
                criador=role.criador,
                participantes=",".join(role.participantes)
            ))
            db.commit()

    def listar(self) -> List[RoleTeste]:
        with get_session() as db:
            rows = db.query(Role).all()
            return [Role(r.titulo, r.descricao, r.data, r.hora,
                         r.criador,
                         r.participantes.split(",") if r.participantes else [])
                    for r in rows]

    def salvar_todos(self, lista_roles: List[RoleTeste]) -> None:
        with get_session() as db:
            db.query(Role).delete()
            for role in lista_roles:
                db.add(Role(
                    titulo=role.titulo,
                    descricao=role.descricao,
                    data=role.data,
                    hora=role.hora,
                    criador=role.criador,
                    participantes=",".join(role.participantes)
                ))
            db.commit()
