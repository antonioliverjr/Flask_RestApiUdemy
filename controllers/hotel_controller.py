from flask_restx import Namespace, Resource, marshal
from config.dependecy_injection import DependencyInjection
from models.hotel_dto import HotelDto
from models.help_dto import HelpsDto
from services.hotel_service import HotelService
from services.city_service import CityService
from config.jwt import Authorize


hotel = Namespace('hotels', description="Hotels operations Get, Get/{id}, Post, Put, Delete")
hotel_dto = hotel.model('hotel', HotelDto.response())
DependencyInjection.register_ioc()
hotelService = HotelService()
cityService = CityService()

@hotel.route('/')
class HotelController(Resource):
    @hotel.doc('Hotel List')
    @hotel.expect(HelpsDto.pagination())
    @hotel.response(code=200, description='Hotel list is Successfully return.', model=[hotel_dto])
    @hotel.response(code=404, description='Hotel list is empty')
    def get(self):
        '''Return Hotel List'''
        args = HelpsDto.pagination()
        data = args.parse_args()
        hotel = hotelService.return_list_pagination(**data)
        if len(hotel) == 0:
            return marshal(hotel, hotel_dto), 404
        return marshal(hotel, hotel_dto), 200

    @hotel.doc('Create a Hotel')
    @hotel.expect(HotelDto.request())
    @hotel.response(code=201, description='Hotel Successfully Create.', model=hotel_dto)
    @hotel.response(code=400, description='There was an error creating in the service.')
    @hotel.response(code=404, description='The City is not created in Cities.')
    @Authorize.token('user', 'admin')
    def post(self):
        '''Register Hotel'''
        args = HotelDto.request()
        data = args.parse_args()
        if not cityService.search_by_name(data['city']):
            return HelpsDto.message('The City {} informed not registered.'.format(data['city'])), 404
        try:
            hotel = hotelService.create(**data)
        except Exception as ex:
            return HelpsDto.message(str(ex)), 400
        return marshal(hotel, hotel_dto), 201


@hotel.route('/<int:id>')
@hotel.param('id', 'Hotel Id')
class HotelControllerId(Resource):
    @hotel.doc('Return a Hotel')
    @hotel.response(code=200, description='Hotel successfully return.', model=hotel_dto)
    @hotel.response(code=404, description='The Hotel is not created in Hotels')
    @Authorize.token('user', 'admin')
    def get(self, id:int):
        '''Return a Hotel'''
        hotel = hotelService.return_by_id(id)
        if hotel is None:
            return HelpsDto.message(f'Id not found, Id:{id} was provided.'), 404
        return marshal(hotel, hotel_dto), 200

    @hotel.doc('Update a Hotel')
    @hotel.expect(HotelDto.request())
    @hotel.response(code=200, description='Hotel successfully return.', model=hotel_dto)
    @hotel.response(code=400, description='There was an error updating the service')
    @hotel.response(code=404, description='The Hotel ou City is not created.')
    @Authorize.token('user', 'admin')
    def put(self, id:int):
        '''Updating Hotel'''
        args = HotelDto.request()
        data = args.parse_args()
        if not hotelService.return_by_id(id):
            return HelpsDto.message(f'Id not found, Hotel Id: {id} was provided.'), 404
        if cityService.search_by_name(data['city']):
            return HelpsDto.message('The City {} informed not registered.'.format(data['city'])), 404        
        data['id'] = id
        try:
            hotel = hotelService.update(**data)
        except Exception as ex:
            return HelpsDto.message(str(ex)), 400
        return marshal(hotel, hotel_dto), 200

    @hotel.doc('Delete a Hotel')
    @hotel.response(code=200, description='Hotel successfully removed.')
    @hotel.response(code=400, description='Error in delete service')
    @hotel.response(code=404, description='The hotel is not created in Hotels')
    @Authorize.token('admin')
    def delete(self, id:int):
        '''Remove Hotel'''
        if hotelService.return_by_id(id):
            try:
                hotelService.remove(id)
            except Exception as ex:
                return HelpsDto.message(str(ex)), 400
            return HelpsDto.message('The registration was successfully removed.'), 200
        return HelpsDto.message(f'Id not found, Id: {id} was provided.'), 404
