from config.app import server
from flask_restx import Resource
from views.city_dto import CityDto
from views.help_dto import HelpsDto
from services.city_service import CityService

api = server.api
city = api.namespace('cities', description="Cities operations Get, Get/{id}, Post, Put, Delete")
city_dto = city.model('city', CityDto.response())
#message_dto = city.model('message', HelpsDto.message())

@city.route('/')
class CityController(Resource):
    @city.doc('Cities List')
    @city.expect(HelpsDto.pagination())
    @city.response(code=200, description='City list is Successfully return.', model=city_dto)
    @city.response(code=404, description='City list is empty')
    def get(self):
        cityService = CityService()
        args = HelpsDto.pagination()
        data = args.parse_args()
        city = cityService.list(offset=data['page'], limit=data['limit'])
        if len(city) != 0:            
            return city, 200
        else:
            return city, 404

    @city.doc('Insert a City')
    @city.expect(CityDto.request())
    @city.response(code=201, description='City Successfully Create.', model=city_dto)
    @city.response(code=400, description='There was an error creating in the service or the city already exists.')
    def post(self):
        cityService = CityService()
        args = CityDto.request()
        data = args.parse_args()
        if cityService.search(data['name']):
            message = {'message': '{} already registered.'.format(data['name'])}
            return message, 400
        try:
            city = cityService.create(data['name'], data['uf'])
        except Exception as ex:
            message = {'message': str(ex)}
            return message, 400
        return city, 201

@city.route('/<int:id>')
@city.param('id', 'City Id')
class CityControllerId(Resource):
    @city.doc('Return a City')
    @city.response(code=200, description='City successfully return.', model=city_dto)
    @city.response(code=404, description='The City is not created in Cities')
    def get(self, id:int):
        cityService = CityService()
        city = cityService.list_id(id)
        if city is None:
            message = {'message': f'Id not found, Id: {id} was provided.'}
            return message, 404
        return city, 200

    @city.doc('Uptade a City')
    @city.expect(CityDto.request())
    @city.response(code=200, description='City successfully return.', model=city_dto)
    @city.response(code=400, description='There was an error updating the service')
    @city.response(code=404, description='The City is not created in Cities')
    def put(self, id:int):
        cityService = CityService()
        args = CityDto.request()
        data = args.parse_args()
        if cityService.list_id(id):
            try:
                city = cityService.update(id, **data)
            except Exception as ex:
                message = {'message': str(ex)}
                return message, 400
            return city, 200
        message = {'message': f'Id not found, Id: {id} was provided.'}
        return message, 404

    @city.doc('Remove a City')
    @city.response(code=200, description='City successfully removed.')
    @city.response(code=400, description='There was an error deleting the service')
    @city.response(code=404, description='The city is not created in Cities')
    def delete(self, id:int):
        cityService = CityService()
        if cityService.list_id(id):
            try:
                cityService.remove(id)
            except Exception as ex:
                message = {'message': str(ex)}
                return message, 400
            message = {'message': 'The registration was successfully removed.'}
            return message, 200
        message = {'message': f'Id not found, Id: {id} was provided.'}
        return message, 404
