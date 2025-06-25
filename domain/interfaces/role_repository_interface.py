from abc import ABC, abstractmethod
from typing import List
from domain.role import RoleTeste


class RoleRepositoryInterface(ABC):

    # ▸ Escrita
    @abstractmethod
    def salvar(self, role: RoleTeste) -> None: ...

    @abstractmethod
    def salvar_todos(self, lista_roles: List[RoleTeste]) -> None: ...

    # ▸ Leitura
    @abstractmethod
    def listar(self) -> List[RoleTeste]: ...
