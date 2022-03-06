from flask_restful import Resource, marshal
from views.hotel import HotelsInputDto, HotelsOutputDto
from repositories.hotel import HotelRepository
from repositories.city import CityRepository


class HotelController(Resource):
    def get(self, id:int = None):
        hotelRepository = HotelRepository()
        if id is not None:
            result = hotelRepository.list_id(id)
            if result is None:
                return {'Error': f'Hotel com o Id: {id} não localizado'}, 400
            return result.to_dict()
        
        result = hotelRepository.list()
        if len(result) == 0:
            return {'Error': 'Não há items para listar'}, 400
        return result
    
    def post(self):
        data = HotelsInputDto.data()
        hotelRepository = HotelRepository()
        cityRepository = CityRepository()
        city_object = cityRepository.search(data.city)
        if city_object is None:
            return {'error': 'A Cidade informada não encontra-se cadastrada.'}, 400
        
        try:
            result = hotelRepository.create(data.name, data.stars, data.daily, city_object)
        except Exception as ex:
            return {'Error': ex}, 400
        
        return result, 201
    
    def put(self, id:int):
        pass

    def delete(self, id:int):
        pass