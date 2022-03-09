from flask import request
from flask_restful import Resource
from flask_apispec import doc, use_kwargs, marshal_with
from flask_apispec.views import MethodResource
from views.city_dto import CityRequestDto, CityResponseDto
from views.help_dto import MessageResponseDto, RouteArgsDto,PaginationArgsDto
from repositories.city_repository import CityRepository
import json

@doc(tags=['Cities'])
class CityController(MethodResource, Resource):
    @doc(description='List of Cities')
    @use_kwargs(PaginationArgsDto, location='query')
    @marshal_with(CityResponseDto(many=True), description='Success', code=200)
    @marshal_with(CityResponseDto(many=True), description='Error', code=404)
    @marshal_with(MessageResponseDto, description='Error Page or Limit not a value reference.', code=422)
    def get(self, **kwargs):
        cityRepository = CityRepository()
        data = PaginationArgsDto().load(kwargs)    
        city = cityRepository.list(offset=data['page'], limit=data['limit'])
        if len(city) != 0:            
            return city, 200
        else:
            return city, 404

    @doc(description='Create City.')
    @use_kwargs(CityRequestDto, location='json')
    @marshal_with(CityResponseDto, description='Success', code=201)
    @marshal_with(MessageResponseDto, description='Error', code=400)
    def post(self, **kwargs):
        data = json.loads(request.data)
        cityRepository = CityRepository()
        if cityRepository.search(data['name']):
            message = {'message': '{} já cadastrada.'.format(data['name'])}
            return message, 400
        try:
            city = cityRepository.create(data['name'], data['uf'])
        except Exception as ex:
            message = {'message': str(ex)}
            return message, 400
        return city, 201


@doc(tags=['Cities'])
class CityControllerId(MethodResource, Resource):
    @doc(description='Return City')
    @marshal_with(CityResponseDto, description='Success', code=200)
    @marshal_with(MessageResponseDto, description='Error', code=404)
    def get(self, id:int):
        cityRepository = CityRepository()
        result = cityRepository.list_id(id)
        if result is None:
            result = {'message': f'Id não localizado, verifique Id:{id} foi o informado.'}
            return result, 404
        return result, 200
        
'''
    @doc(description='Update City.')
    @use_kwargs(CityRequestDto, location='json')
    @marshal_with(CityResponseDto, description='Success', code=200)
    @marshal_with(MessageResponseDto, description='Error', code=400)
    @marshal_with(MessageResponseDto, description='Error', code=404)
    def put(self, id:int, **kwargs):
        data = json.loads(request.data)
        cityRepository = CityRepository()
        if cityRepository.list_id(id):
            try:
                city = cityRepository.update(id, **data)
            except Exception as ex:
                result = {'message': str(ex)}
                return result, 400
            return city, 200
        result = {'message': f'Id não localizado, verifique Id:{id} foi o informado.'}
        return result, 404

    @doc(description='Remove City.')
    @marshal_with(MessageResponseDto, description='Success', code=200)
    @marshal_with(MessageResponseDto, description='Error', code=400)
    @marshal_with(MessageResponseDto, description='Error', code=404)
    def delete(self, id:int):
        cityRepository = CityRepository()
        if cityRepository.list_id(id):
            try:
                cityRepository.remove(id)
            except Exception as ex:
                result = {'message': str(ex)}
                return result, 400
            result = {'message': 'Cidade removida com sucesso.'}
            return result, 200
        result = {'message': f'Id não localizado, verifique Id:{id} foi o informado.'}
        return result, 404
'''