from typing import Union, List
from data.context import Context
from data.interfaces.icity_repository import ICityRepository
from entities.city_entity import CityModel


class CityRepository(ICityRepository):
    def __init__(self) -> None:
        self.conn = Context()

    def get(self, offset:int, limit:int) -> List[CityModel]:
        offset = (offset - 1) * limit
        return self.conn.session.query(CityModel).offset(offset).limit(limit).all()

    def get_id(self, id:int) -> Union[CityModel, None]:
        return self.conn.session.query(CityModel).filter_by(id=id).first()

    def add(self, name:str, uf:str) -> Union[CityModel, Exception]:
        city = CityModel(name.upper(), uf.upper())
        try:
            self.conn.session.add(city)
            self.conn.save()
        except Exception as ex:
            return ex

        result = self.search(name)       
        return result

    def update(self, id:int, **city) -> Union[CityModel, Exception]:
        city['name'] = city['name'].upper()
        city['uf'] = city['uf'].upper()
        try:
            self.conn.session.query(CityModel).filter_by(id=id).update(city, synchronize_session=False)
            self.conn.save()
        except Exception as ex:
            return ex
        return self.list_id(id)
    
    def delete(self, id:int) -> Union[bool, Exception]:
        try:
            self.conn.session.query(CityModel).filter_by(id=id).delete(synchronize_session=False)
            self.conn.save()
        except Exception as ex:
            return ex
        return True

    def search(self, city_name:str) -> Union[CityModel, None]:
        return self.conn.session.query(CityModel).filter_by(name=city_name.upper()).first()