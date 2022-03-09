from flask_restx import reqparse, fields


class HelpsDto:
    @staticmethod
    def pagination():
        args = reqparse.RequestParser()
        args.add_argument('page', type=int, default=1, help='Page value greater than 1', location='args')
        args.add_argument('limit', type=int, default=25, help='limit value greater than 1', location='args')
        return args
    
    
    @staticmethod
    def message():
        message = {
            'message': fields.String
        }
        return message
