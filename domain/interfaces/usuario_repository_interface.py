from abc import ABC, abstractmethod
from typing import Optional
from domain.usuario import UsuarioTeste


class UsuarioRepositoryInterface(ABC):
    """Contrato para repositórios de Usuário."""

    @abstractmethod
    def salvar(self, usuario: UsuarioTeste) -> None: ...

    @abstractmethod
    def buscar_por_email_senha(
        self, email: str, senha: str
    ) -> Optional[UsuarioTeste]: ...
