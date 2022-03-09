from config.app import server
from flask_restx import Resource
from views.hotel_dto import HotelDto
from views.help_dto import HelpsDto
from services.hotel_service import HotelService
from services.city_service import CityService


api = server.api
hotel = api.namespace('hotels', description="Hotels operations Get, Get/{id}, Post, Put, Delete")
hotel_dto = hotel.model('hotel', HotelDto.response())
#message_dto = hotel.model('message', HelpsDto.message())

@hotel.route('/')
class HotelController(Resource):
    @hotel.doc('Hotel List')
    @hotel.expect(HelpsDto.pagination())
    @hotel.response(code=200, description='Hotel list is Successfully return.', model=hotel_dto)
    @hotel.response(code=404, description='Hotel list is empty')
    def get(self):
        hotelService = HotelService()
        args = HelpsDto.pagination()
        data = args.parse_args()
        hotel = hotelService.list(offset=data['page'], limit=data['limit'])
        if len(hotel) == 0:
            return hotel, 404
        return hotel, 200

    @hotel.doc('Create a Hotel')
    @hotel.expect(HotelDto.request())
    @hotel.response(code=201, description='Hotel Successfully Create.', model=hotel_dto)
    @hotel.response(code=400, description='There was an error creating in the service.')
    @hotel.response(code=404, description='The City is not created in Cities.')
    def post(self):
        hotelService = HotelService()
        cityService = CityService()
        args = HotelDto.request()
        data = args.parse_args()
        city = cityService.search(data['city'])
        if city is None:
            message = {'message': 'The City {} informed not registered.'.format(data['city'])}
            return message, 404
        try:
            hotel = hotelService.create(data['name'], data['stars'], data['daily'], city, data['status'])
        except Exception as ex:
            message = {'message': str(ex)}
            return message, 400
        return hotel, 201


@hotel.route('/<int:id>')
@hotel.param('id', 'Hotel Id')
class HotelControllerId(Resource):
    @hotel.doc('Return a Hotel')
    @hotel.response(code=200, description='Hotel successfully return.', model=hotel_dto)
    @hotel.response(code=404, description='The Hotel is not created in Hotels')
    def get(self, id:int):
        hotelService = HotelService()
        hotel = hotelService.list_id(id)
        if hotel is None:
            message = {'message': f'Id not found, Id:{id} was provided.'}
            return message, 404
        return hotel, 200

    @hotel.doc('Update a Hotel')
    @hotel.expect(HotelDto.request())
    @hotel.response(code=200, description='Hotel successfully return.', model=hotel_dto)
    @hotel.response(code=400, description='There was an error updating the service')
    @hotel.response(code=404, description='The City is not created in Cities')
    def put(self, id:int):
        hotelService = HotelService()
        cityService = CityService()
        args = HotelDto.request()
        data = args.parse_args()
        city = cityService.search(data['city'])
        if city is None:
            message = {'message': 'The City {} informed not registered.'.format(data['city'])}
            return message, 404
        try:
            hotel = hotelService.update(id, data['name'], data['stars'], data['daily'], city
            , data['status'])
        except Exception as ex:
            message = {'message': str(ex)}
            return message, 400
        return hotel, 200

    @hotel.doc('Delete a Hotel')
    @hotel.response(code=200, description='Hotel successfully removed.')
    @hotel.response(code=400, description='Error in delete service')
    @hotel.response(code=404, description='The hotel is not created in Hotels')
    def delete(self, id:int):
        hotelService = HotelService()
        if hotelService.list_id(id):
            try:
                hotelService.remove(id)
            except Exception as ex:
                message = {'message': str(ex)}
                return message, 400
            message = {'message': 'The registration was successfully removed.'}
            return message, 200
        message = {'message': f'Id not found, Id: {id} was provided.'}
        return message, 404
