from typing import List
from models.hotel import HotelModel
from models.city import CityModel


class HotelRepository(HotelModel):
    def list(self):
        pass
    
    def list_id(self):
        pass
    
    def create(cls, name:str, stars:int, daily:float, cities:List[CityModel]):
        pass

    def uptade(self):
        pass

    def delete(self):
        pass