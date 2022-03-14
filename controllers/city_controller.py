from flask_restx import Namespace, Resource, marshal
from config.dependecy_injection import DependencyInjection
from models.city_dto import CityDto
from models.help_dto import HelpsDto
from services.city_service import CityService
from config.jwt import Authorize


city = Namespace('cities', description="Cities operations Get, Get/{id}, Post, Put, Delete")
city_dto = city.model('city', CityDto.response())
DependencyInjection.register_ioc()
cityService = CityService()

@city.route('/')
class CityController(Resource):
    @city.doc('Cities List')
    @city.expect(HelpsDto.pagination())
    @city.response(code=200, description='City list is Successfully return.', model=[city_dto])
    @city.response(code=404, description='City list is empty')
    def get(self):
        args = HelpsDto.pagination()
        data = args.parse_args()
        city = cityService.return_list_pagination(**data)
        if len(city) != 0:            
            return marshal(city, city_dto), 200
        else:
            return marshal(city, city_dto), 404

    @city.doc('Insert a City')
    @city.expect(CityDto.request())
    @city.response(code=201, description='City Successfully Create.', model=city_dto)
    @city.response(code=400, description='There was an error creating in the service or the city already exists.')
    @Authorize.token('user', 'admin')
    def post(self):
        args = CityDto.request()
        data = args.parse_args()
        if cityService.search_by_name(data['name']):
            return HelpsDto.message('{} already registered.'.format(data['name'])), 400
        try:
            city = cityService.create(**data)
        except Exception as ex:
            return HelpsDto.message(str(ex)), 400
        return marshal(city, city_dto), 201

@city.route('/<int:id>')
@city.param('id', 'City Id')
class CityControllerId(Resource):
    @city.doc('Return a City')
    @city.response(code=200, description='City successfully return.', model=city_dto)
    @city.response(code=404, description='The City is not created in Cities')
    @Authorize.token('user', 'admin')
    def get(self, id:int):
        city = cityService.return_by_id(id)
        if city is None:
            return HelpsDto.message(f'Id not found, Id: {id} was provided.'), 404
        return marshal(city, city_dto), 200

    @city.doc('Uptade a City')
    @city.expect(CityDto.request())
    @city.response(code=200, description='City successfully return.', model=city_dto)
    @city.response(code=400, description='There was an error updating the service')
    @city.response(code=404, description='The City is not created in Cities')
    @Authorize.token('user', 'admin')
    def put(self, id:int):
        args = CityDto.request()
        data = args.parse_args()
        if cityService.return_by_id(id):
            try:
                city = cityService.update(id, **data)
            except Exception as ex:
                return HelpsDto.message(str(ex)), 400
            return marshal(city, city_dto), 200
        return HelpsDto.message(f'Id not found, Id: {id} was provided.'), 404

    @city.doc('Remove a City')
    @city.response(code=200, description='City successfully removed.')
    @city.response(code=400, description='There was an error deleting the service')
    @city.response(code=404, description='The city is not created in Cities')
    @Authorize.token('admin')
    def delete(self, id:int):
        if cityService.list_id(id):
            try:
                cityService.remove(id)
            except Exception as ex:
                return HelpsDto.message(str(ex)), 400
            return HelpsDto.message('The registration was successfully removed.'), 200
        return HelpsDto.message(f'Id not found, Id: {id} was provided.'), 404
