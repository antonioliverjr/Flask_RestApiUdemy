from typing import Union, List
from data.context import Context
from models.hotel import HotelModel
from models.city import CityModel


class HotelRepository():
    def __init__(self) -> None:
        self.conn = Context()
    
    def list(self) -> List[HotelModel]:
        return self.conn.session.query(HotelModel).all()
    
    def list_id(self, id:int) -> Union[HotelModel, None]:
        return self.conn.session.query(HotelModel).filter_by(id=id).first()

    def create(self, name:str, stars:int, daily:float, city:CityModel):
        hotel = HotelModel(name, stars, daily, city_id=city)
        try:
            self.conn.session.add(hotel)
            self.conn.save()
        except Exception as ex:
            return ex
        return hotel