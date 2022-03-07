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
                result = {'message': f'Id não localizado, verifique Id:{id} foi o informado.'}
                return marshal(result, HotelsOutputDto.message()), 404
            return marshal(result, HotelsOutputDto.response()), 200
        
        result = hotelRepository.list()
        if len(result) == 0:
            return marshal(result, HotelsOutputDto.response()), 404
        return marshal(result, HotelsOutputDto.response()), 200
    
    def post(self):
        data = HotelsInputDto.request()
        hotelRepository = HotelRepository()
        cityRepository = CityRepository()
        city_obj = cityRepository.search(data.city)
        if city_obj is None:
            result = {'message': f'A Cidade {data.city} informada não encontra-se cadastrada.'}
            return marshal(result, HotelsOutputDto.message()), 400
        try:
            result = hotelRepository.create(data.name, data.stars, data.daily, city_obj)
        except Exception as ex:
            result = {'message': str(ex)}
            return marshal(result, HotelsOutputDto.message()), 400
        return marshal(result, HotelsOutputDto.response()), 201
    
    def put(self, id:int):
        data = HotelsInputDto.request()
        hotelRepository = HotelRepository()
        cityRepository = CityRepository()
        city_obj = cityRepository.search(data.city)
        if city_obj is None:
            result = {'message': f'A Cidade {data.city} informada não encontra-se cadastrada.'}
            return marshal(result, HotelsOutputDto.message()), 400
        try:
            result = hotelRepository.update(id, data.name, data.stars, data.daily, city_obj
            , data.status if data.status is not None else True)
        except Exception as ex:
            result = {'message': str(ex)}
            return marshal(result, HotelsOutputDto.message()), 400
        return marshal(result, HotelsOutputDto.response()), 201

    def delete(self, id:int):
        hotelRepository = HotelRepository()
        if hotelRepository.list_id(id):
            try:
                hotelRepository.remove(id)
            except Exception as ex:
                result = {'message': str(ex)}
                return marshal(result, HotelsOutputDto.message()), 400
            result = {'message': 'O cadastro foi removido com sucesso.'}
            return marshal(result, HotelsOutputDto.message()), 200
        result = {'message': f'Id não localizado, verifique Id:{id} foi o informado.'}
        return marshal(result, HotelsOutputDto.message()), 404