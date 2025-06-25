# infra/repositories/usuario_repository.py
from typing import Optional
from domain.usuario import UsuarioTeste
from infra.db.database import get_session, Usuario        # modelo SQLAlchemy
from domain.interfaces.usuario_repository_interface import (
    UsuarioRepositoryInterface,
)


class UsuarioRepository(UsuarioRepositoryInterface):
    """Implementação concreta usando SQLAlchemy."""

    # ───── Escrita ─────
    def salvar(self, usuario: UsuarioTeste) -> None:
        with get_session() as db:
            db.add(
                Usuario(
                    nome=usuario.nome,
                    email=usuario.email,
                    senha=usuario.senha,
                )
            )
            db.commit()

    # ───── Leitura ─────
    def buscar_por_email_senha(
        self, email: str, senha: str
    ) -> Optional[UsuarioTeste]:
        with get_session() as db:
            row = (
                db.query(Usuario)
                .filter_by(email=email, senha=senha)
                .first()
            )
            return (
                UsuarioTeste(row.nome, row.email, row.senha) if row else None
            )
