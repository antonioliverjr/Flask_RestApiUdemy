from flask import request
from flask_restful import Resource
from flask_apispec import doc, use_kwargs, marshal_with
from flask_apispec.views import MethodResource
from views.hotel_dto import HotelRequestDto, HotelResponseDto
from views.help_dto import MessageResponseDto, PaginationArgsDto
from repositories.hotel_repository import HotelRepository
from repositories.city_repository import CityRepository
import json


@doc(tags=['Hotels'])
class HotelController(MethodResource, Resource):
    @doc(description='List of Hotels.')
    @use_kwargs(PaginationArgsDto, location='query')
    @marshal_with(HotelResponseDto(many=True), description='Success', code=200)
    @marshal_with(MessageResponseDto, description='Error', code=404)
    @marshal_with(MessageResponseDto, description='Error Page or Limit not a value reference.', code=422)
    def get(self, **kwargs):
        hotelRepository = HotelRepository()
        data = PaginationArgsDto().load(kwargs)
        result = hotelRepository.list(offset=data['page'], limit=data['limit'])
        if len(result) == 0:
            return result, 404
        return result, 200
    
    @doc(description='Create Hotel.')
    @use_kwargs(HotelRequestDto, location='json')
    @marshal_with(HotelResponseDto, description='Success', code=201)
    @marshal_with(MessageResponseDto, description='Error', code=400)
    def post(self, **kwargs):
        data = json.loads(request.data)
        hotelRepository = HotelRepository()
        cityRepository = CityRepository()
        city_obj = cityRepository.search(data['city'])
        if city_obj is None:
            result = {'message': 'A Cidade {} informada não encontra-se cadastrada.'.format(data['city'])}
            return result, 400
        try:
            result = hotelRepository.create(data['name'], data['stars'], data['daily'], city_obj)
        except Exception as ex:
            result = {'message': str(ex)}
            return result, 400
        return result, 201
    
    
@doc(tags=['Hotels'])
class HotelControllerId(MethodResource, Resource):
    @doc(description='Return Hotel.')
    @marshal_with(HotelResponseDto, description='Success', code=200)
    @marshal_with(MessageResponseDto, description='Error', code=400)
    def get(self, id:int):
        hotelRepository = HotelRepository()
        result = hotelRepository.list_id(id)
        if result is None:
            result = {'message': f'Id não localizado, verifique Id:{id} foi o informado.'}
            return result, 404
        return result, 200

    @doc(description='Update Hotel.')
    @use_kwargs(HotelRequestDto, location='json')
    @marshal_with(HotelResponseDto, description='Success', code=200)
    @marshal_with(MessageResponseDto, description='Error', code=400)
    @marshal_with(MessageResponseDto, description='Error', code=404)
    def put(self, id:int, **kwargs):
        data = json.loads(request.data)
        hotelRepository = HotelRepository()
        cityRepository = CityRepository()
        city_obj = cityRepository.search(data['city'])
        if city_obj is None:
            result = {'message': 'A Cidade {} informada não encontra-se cadastrada.'.format(data['city'])}
            return result, 404
        try:
            result = hotelRepository.update(id, data['name'], data['stars'], data['daily'], city_obj
            , data['status'] if data['status'] is not None else True)
        except Exception as ex:
            result = {'message': str(ex)}
            return result, 400
        return result, 200

    @doc(description='Remove Hotel.')
    @marshal_with(MessageResponseDto, description='Success', code=200)
    @marshal_with(MessageResponseDto, description='Error', code=400)
    @marshal_with(MessageResponseDto, description='Error', code=404)
    def delete(self, id:int):
        hotelRepository = HotelRepository()
        if hotelRepository.list_id(id):
            try:
                hotelRepository.remove(id)
            except Exception as ex:
                result = {'message': str(ex)}
                return result, 400
            result = {'message': 'O cadastro foi removido com sucesso.'}
            return result, 200
        result = {'message': f'Id não localizado, verifique Id:{id} foi o informado.'}
        return result, 404
