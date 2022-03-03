from flask_restful import reqparse, fields


class HotelsInputDto():
    @staticmethod
    def data():
        arguments = reqparse.RequestParser()
        arguments.add_argument('name', type=str, required=True, help='Name is required and only string')
        arguments.add_argument('stars', type=int, required=True, help='Stars is required and only integer')
        arguments.add_argument('daily', type=float, required=True, help='Daily is required and only decimal')
        arguments.add_argument('city', type=str, action='append', required=True, help='City is required and only string')
        return arguments.parse_args()

class HotelsOutputDto():
    @staticmethod
    def data():
        data = {
            'id': fields.Integer,
            'name': fields.String,
            'stars': fields.Integer,
            'daily': fields.Float,
            'city': fields.List(fields.String)
        }
        return data