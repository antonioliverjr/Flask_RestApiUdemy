from flask_restful import reqparse, fields
from views.base_dto import BaseDto


class CityModelViewDto(BaseDto):
    @staticmethod
    def request():
        arguments = reqparse.RequestParser()
        arguments.add_argument('name', type=str, required=True, help='Name is required.')
        arguments.add_argument('uf', type=str, required=True, help='Uf is required.')

        return arguments.parse_args()

    @staticmethod
    def response():
        response = {
            'id': fields.Integer,
            'name': fields.String,
            'uf': fields.String
        }
        return response
