from flask_restful import reqparse, fields


class HotelsInputDto():
    @staticmethod
    def request():
        arguments = reqparse.RequestParser()
        arguments.add_argument('name', type=str, required=True, help='Name is required and only string')
        arguments.add_argument('stars', type=int, required=True, help='Stars is required and only integer')
        arguments.add_argument('daily', type=float, required=True, help='Daily is required and only decimal')
        arguments.add_argument('city', type=str, required=True, help='City is required and only string')
        arguments.add_argument('status', type=bool, help='Status is not required and default value is True')
        return arguments.parse_args()

class HotelsOutputDto():
    @staticmethod
    def response():
        response = {
            'id': fields.Integer,
            'name': fields.String,
            'stars': fields.Integer,
            'daily': fields.Float,
            'city': {
                'city.id': fields.Integer, 
                'city.name': fields.String,
                'city.uf': fields.String
            },
            'status': fields.Boolean
        }
        return response
    
    @staticmethod
    def message():
        message = {
            'message': fields.String
        }
        return message