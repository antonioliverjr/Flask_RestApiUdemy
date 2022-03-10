from typing import Union, List
from entities.city_entity import CityModel
from abc import ABC, abstractmethod


class ICityRepository(ABC):
    @abstractmethod
    def get(self, offset:int, limit:int) -> List[CityModel]: pass
    @abstractmethod
    def get_id(self, id:int) -> Union[CityModel, None]: pass
    @abstractmethod
    def add(self, name:str, uf:str) -> Union[CityModel, Exception]: pass
    @abstractmethod
    def update(self, id:int, **city) -> Union[CityModel, Exception]: pass
    @abstractmethod
    def delete(self, id:int) -> Union[bool, Exception]: pass
    @abstractmethod
    def search(self, city_name:str) -> Union[CityModel, None]: pass