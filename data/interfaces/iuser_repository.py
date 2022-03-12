from typing import List, Union
from abc import ABC, abstractmethod
from entities.identity.user_entity import UserModel


class IUserRepository(ABC):
    @abstractmethod
    def get(self, offset:int, limit:int) -> List[UserModel]: pass
    @abstractmethod
    def get_id(self, id:int) -> Union[UserModel, None]: pass
    @abstractmethod
    def add(self, username:str, password:str, firstname:str, email:str, role:str, lastname:str=None) -> Union[UserModel, Exception]: pass
    @abstractmethod
    def update(self, id:int, **user) -> Union[UserModel, Exception]: pass
    @abstractmethod
    def delete(self, id:int) -> Union[bool, Exception]: pass
    @abstractmethod
    def search(self, username:str, email:str=None) -> Union[UserModel, None]: pass