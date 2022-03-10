from typing import List, Union
from entities.hotel_entity import HotelModel
from entities.city_entity import CityModel
from abc import ABC, abstractmethod


class IHotelRepository(ABC):
    @abstractmethod
    def get(self, offset:int, limit:int) -> List[HotelModel]: pass
    @abstractmethod
    def get_id(self, id:int) -> Union[HotelModel, None]: pass
    @abstractmethod
    def create(self, name:str, stars:int, daily:float, city:str, status:bool) -> Union[HotelModel, Exception]: pass
    @abstractmethod
    def update(self, id:int, name:str, stars:int, daily:float, city:str, status:bool) -> Union[HotelModel, Exception]: pass
    @abstractmethod
    def delete(self, id:int): pass
    @abstractmethod
    def search(self, hotel_name:str) -> Union[HotelModel, None]: pass