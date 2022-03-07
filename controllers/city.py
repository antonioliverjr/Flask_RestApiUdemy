from flask_restful import Resource, marshal
from views.city import CityModelViewDto
from repositories.city import CityRepository


class CityController(Resource):
    def get(self, id:int = None):
        cityRepository = CityRepository()
        if id is not None:
            result = cityRepository.list_id(id)
            if result is None:
                result = {'message': f'Id não localizado, verifique Id:{id} foi o informado.'}
                return marshal(result, CityModelViewDto.message()), 404
            
            return marshal(result, CityModelViewDto.response()), 200
        
        result = cityRepository.list()
        if len(result) != 0:
            return marshal(result, CityModelViewDto.response()), 200
        else:
            return marshal(result, CityModelViewDto.response()), 404
    
    def post(self):
        data = CityModelViewDto.request()
        cityRepository = CityRepository()
        if cityRepository.search(data.name):
            result = {'message': f'{data.name} já cadastrada.'}
            return marshal(result, CityModelViewDto.message()), 400
        try:
            city = cityRepository.create(data.name, data.uf)
        except Exception as ex:
            result = {'message': str(ex)}
            return marshal(result, CityModelViewDto.message()), 400
        return marshal(city, CityModelViewDto.response()), 201

    def put(self, id:int):
        data = CityModelViewDto.request()
        cityRepository = CityRepository()
        if cityRepository.list_id(id):
            try:
                city = cityRepository.update(id, **data)
            except Exception as ex:
                result = {'message': str(ex)}
                return marshal(result, CityModelViewDto.message()), 400
            return marshal(city, CityModelViewDto.response()), 200
        result = {'message': f'Id não localizado, verifique Id:{id} foi o informado.'}
        return marshal(result, CityModelViewDto.message()), 404

    def delete(self, id:int):
        cityRepository = CityRepository()
        if cityRepository.list_id(id):
            try:
                cityRepository.remove(id)
            except Exception as ex:
                result = {'message': str(ex)}
                return marshal(result, CityModelViewDto.message()), 400
            result = {'message': 'Cidade removida com sucesso.'}
            return marshal(result, CityModelViewDto.message()), 200
        result = {'message': f'Id não localizado, verifique Id:{id} foi o informado.'}
        return marshal(result, CityModelViewDto.message()), 404
        