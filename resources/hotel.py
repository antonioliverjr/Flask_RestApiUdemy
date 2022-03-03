from flask_restful import Resource, marshal_with
from models_dto.hotel import HotelsInputDto, HotelsOutputDto
from repositories.hotel import HotelRepository
from repositories.city import CityRepository


class HotelController(Resource):
    @marshal_with(HotelsOutputDto.data())
    def get(self, id:int = None):
        if id is not None:
            return {
                "id": id,
                "name": "Plaza",
                "stars": 4,
                "daily": 250.0,
                "city": [
                    "Camaçari"
                ]
            }
        else:
            return {
                "id": 1,
                "name": "Plaza",
                "stars": 4,
                "daily": 250.0,
                "city": [
                    "Camaçari"
                ]
            }
    
    @marshal_with(HotelsOutputDto.data())
    def post(self):
        data = HotelsInputDto.data()
        hotel = HotelRepository()
        city = CityRepository()
        cities = []
        for city_name in data.city:
            find_city = city.search(city_name)
            if find_city is not None:
                cities.append(find_city)
        try:
            result = hotel.create(data.name, data.stars, data.daily, cities)
        except ValueError as ex:
            return {'message': ex}
        except Exception as ex:
            return {'Error': ex}
        return result, 201
    
    def put(self, id:int):
        pass

    def delete(self, id:int):
        pass