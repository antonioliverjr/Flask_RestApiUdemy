from typing import Union, List
from data.context import Context
from entities.hotel_entity import HotelModel
from entities.city_entity import CityModel


class HotelService():
    def __init__(self) -> None:
        self.conn = Context()
    
    def list(self, offset:int, limit:int) -> List[HotelModel]:
        offset = (offset - 1) * limit
        return self.conn.session.query(HotelModel).offset(offset).limit(limit).all()
    
    def list_id(self, id:int) -> Union[HotelModel, None]:
        return self.conn.session.query(HotelModel).filter_by(id=id).first()

    def create(self, name:str, stars:int, daily:float, city:CityModel, status:bool) -> Union[HotelModel, Exception]:
        hotel = HotelModel(name, stars, daily, city, status=status)
        try:
            self.conn.session.add(hotel)
            self.conn.save()
        except Exception as ex:
            return ex
        return self.search(name)
    
    def update(self, id:int, name:str, stars:int, daily:float, city:CityModel
    , status:bool) -> Union[HotelModel, Exception]:
        try:
            self.conn.session.query(HotelModel).filter_by(id=id)\
                .update(
                    {
                        'name': name.upper(),
                        'stars': stars,
                        'daily': daily,
                        'city_id': city.id,
                        'status': status
                    }, synchronize_session=False
                )
            self.conn.save()
        except Exception as ex:
            return ex
        return self.list_id(id)

    def remove(self, id:int):
        try:
            self.conn.session.query(HotelModel).filter_by(id=id).delete()
            self.conn.save()
        except Exception as ex:
            return ex
        return True
    
    def search(self, hotel_name:str) -> Union[HotelModel, None]:
        return self.conn.session.query(HotelModel).filter_by(name=hotel_name.upper()).first()