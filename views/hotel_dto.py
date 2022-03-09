from flask_restx import reqparse, fields
from views.city_dto import CityDto
from controllers.city_controller import city_dto


class HotelDto:
    @staticmethod
    def request():
        args = reqparse.RequestParser()
        args.add_argument('name', type=str, required=True, help='Name is required and only string', location='json')
        args.add_argument('stars', type=int, required=True, help='Stars is required and only integer', location='json')
        args.add_argument('daily', type=float, required=True, help='Daily is required and only decimal', location='json')
        args.add_argument('city', type=str, required=True, help='City is required and only string', location='json')
        args.add_argument('status', type=bool, default=True,help='Status is not required and default value is True', location='json')
        return args

    @staticmethod
    def response():
        response = {
            'id': fields.Integer,
            'name': fields.String,
            'stars': fields.Integer,
            'daily': fields.Float,
            'city': fields.Nested(city_dto),
            'status': fields.Boolean
        }
        return response
