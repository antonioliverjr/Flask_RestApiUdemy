import inject
from typing import Union, List
from data.interfaces.ihotel_repository import IHotelRepository
from entities.hotel_entity import HotelModel


class HotelService():
    @inject.autoparams()
    def __init__(self, hotelRepository: IHotelRepository) -> None:
        self.hotelRepository = hotelRepository()
    
    def return_list_pagination(self, page:int, limit:int) -> List[HotelModel]:
        return self.hotelRepository.get(offset=page, limit=limit)
    
    def return_by_id(self, id:int) -> Union[HotelModel, None]:
        return self.hotelRepository.get_id(id)

    def create(self, **data) -> Union[HotelModel, Exception]:
        return self.hotelRepository.create(**data)
    
    def update(self, **data) -> Union[HotelModel, Exception]:
        return self.hotelRepository.update(**data)

    def remove(self, id:int):
        return self.hotelRepository.delete(id)
    
    def search_by_name(self, hotel_name:str) -> Union[HotelModel, None]:
        return self.hotelRepository.search(hotel_name)