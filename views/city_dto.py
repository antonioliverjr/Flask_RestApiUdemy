from flask_restx import reqparse, fields


class CityDto:
    @staticmethod
    def request():
        args = reqparse.RequestParser()
        args.add_argument('name', type=str, required=True, help='Name is required.', location='json')
        args.add_argument('uf', type=str, required=True, help='Uf is required.', location='json')
        return args

    @staticmethod
    def response():
        response = {
            'id': fields.Integer,
            'name': fields.String,
            'uf': fields.String
        }
        return response
