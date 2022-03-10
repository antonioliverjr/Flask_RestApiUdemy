from typing import Union, List
from entities.city_entity import CityModel
import inject
from data.interfaces.icity_repository import ICityRepository


class CityService():
    @inject.autoparams()
    def __init__(self, cityRepository: ICityRepository) -> None:
        self.cityRepository = cityRepository()

    def return_list_pagination(self, page:int, limit:int) -> List[CityModel]:
        return self.cityRepository.get(offset=page, limit=limit)

    def return_by_id(self, id:int) -> Union[CityModel, None]:
        return self.cityRepository.get_id(id)

    def create(self, name:str, uf:str) -> Union[CityModel, Exception]:
        return self.cityRepository.add(name, uf)

    def update(self, id:int, **city) -> Union[CityModel, Exception]:
        return self.cityRepository.update(id, **city)
    
    def remove(self, id:int) -> Union[bool, Exception]:
        return self.cityRepository.delete(id)

    def search_by_name(self, city_name:str) -> Union[CityModel, None]:
        return self.cityRepository.search(city_name)