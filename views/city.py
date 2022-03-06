from flask_restful import reqparse, fields


class CityInputDto():
    @staticmethod
    def request():
        arguments = reqparse.RequestParser()
        arguments.add_argument('name', type=str, required=True, help='Name is required.')
        arguments.add_argument('uf', type=str, required=True, help='Uf is required.')

        return arguments.parse_args()

class CityOutputDto():
    @staticmethod
    def response():
        response = {
            'id': fields.Integer,
            'name': fields.String,
            'uf': fields.String
        }
        return response
    
    @staticmethod
    def message():
        message = {
            'message': fields.String
        }
        return message
