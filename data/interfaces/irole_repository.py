from typing import List, Union
from abc import ABC, abstractmethod
from entities.identity.roles_entity import RoleModel


class IRoleRepository(ABC):
    @abstractmethod
    def get(self) -> List[RoleModel]: pass
    @abstractmethod
    def get_id(self, id:int) -> Union[RoleModel, None]: pass
    @abstractmethod
    def search(self, role:str) -> Union[RoleModel, None]: pass