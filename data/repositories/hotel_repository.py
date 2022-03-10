from typing import Union, List
from data.context import Context
from data.interfaces.ihotel_repository import IHotelRepository
from entities.hotel_entity import HotelModel
from entities.city_entity import CityModel


class HotelRepository(IHotelRepository):
    def __init__(self) -> None:
        self.conn = Context()
    
    def get(self, offset:int, limit:int) -> List[HotelModel]:
        offset = (offset - 1) * limit
        return self.conn.session.query(HotelModel).offset(offset).limit(limit).all()
    
    def get_id(self, id:int) -> Union[HotelModel, None]:
        return self.conn.session.query(HotelModel).filter_by(id=id).first()

    def create(self, name:str, stars:int, daily:float, city:str, status:bool) -> Union[HotelModel, Exception]:
        city = self.conn.session.query(CityModel).filter_by(name=city).first()
        hotel = HotelModel(name, stars, daily, city, status=status)
        try:
            self.conn.session.add(hotel)
            self.conn.save()
        except Exception as ex:
            return ex
        return self.search(name)
    
    def update(self, id:int, name:str, stars:int, daily:float, city:str
    , status:bool) -> Union[HotelModel, Exception]:
        city = self.conn.session.query(CityModel).filter_by(name=city).first()
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
        return self.get_id(id)

    def delete(self, id:int):
        try:
            self.conn.session.query(HotelModel).filter_by(id=id).delete()
            self.conn.save()
        except Exception as ex:
            return ex
        return True
    
    def search(self, hotel_name:str) -> Union[HotelModel, None]:
        return self.conn.session.query(HotelModel).filter_by(name=hotel_name.upper()).first()